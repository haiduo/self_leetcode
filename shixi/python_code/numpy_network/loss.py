import numpy as np

#loss 
def softmax(x, t=1.0, axis=-1):
    x_ = x / t
    x_max = np.max(x_, axis=axis, keepdims=True)
    exps = np.exp(x_ - x_max)
    return exps / np.sum(exps, axis=axis, keepdims=True)


def log_softmax(x, t=1.0, axis=-1):
    x_ = x / t
    if x.ndim > 1:
        x_max = np.max(x_, axis=axis, keepdims=True)
        exps = np.exp(x_ - x_max)
        exp_sum = np.sum(exps, axis=axis, keepdims=True)
    else:
        x_max = np.max(x_, keepdims=True)
        exps = np.exp(x_ - x_max)
        exp_sum = np.sum(exps, keepdims=True)
    return x_ - x_max - np.log(exp_sum)


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

class Loss:
    def loss(self, *args, **kwargs):
        raise NotImplementedError

    def grad(self, *args, **kwargs):
        raise NotImplementedError
    
class SoftmaxCrossEntropy(Loss):

    def __init__(self, T=1.0, weights=None):
        self._weights = np.asarray(weights) if weights is not None else weights
        self._T = T

    def loss(self, logits, labels):
        if logits.ndim > 1:
            nll = -(log_softmax(logits, t=self._T, axis=1) * np.expand_dims(labels, axis=1)).sum(axis=1)
        else:
            nll = -(log_softmax(logits, t=self._T, axis=1) * labels)
        if self._weights is not None:
            nll *= self._weights[np.argmax(logits, axis=1)]
        return np.sum(nll) / labels.shape[0] if logits.ndim > 1 else np.sum(nll)

    def grad(self, logits, labels):
        if logits.ndim > 1:
            grads = softmax(logits, t=self._T) - np.expand_dims(labels, axis=1)
        else:
            grads = softmax(logits, t=self._T) - labels
        if self._weights is not None:
            grads *= self._weights
        return grads / labels.shape[0] if logits.ndim > 1 else grads

class SigmoidCrossEntropy(Loss):
    """let logits = a, label = y, weights[neg] = w1, weights[pos] = w2
    L = - w2 * y * log(1 / (1 + exp(-a)) - w1 * (1-y) * log(exp(-a) / (1 + exp(-a))
      = w1 * a * (1 - y) - (w2 * y - w1 * (y - 1)) * log(sigmoid(a))
    if w1 == w2 == 1:
    L = a * (1 - y) - log(sigmoid(a))

    G = w1 * sigmoid(a) - w2 * y + (w2 - w1) * y * sigmoid(a)
    if w1 == w2 == 1:
    G = sigmoid(a) - y
    """
    def __init__(self, weights=None):
        weights = np.ones(2, dtype=np.float32) if weights is None else weights
        self._weights = np.asarray(weights)

    def loss(self, logits, labels):
        neg_weight, pos_weight = self._weights
        cost = neg_weight * logits * (1 - labels) - \
               (pos_weight * labels - neg_weight * (labels - 1)) * \
               np.log(sigmoid(logits))
        return np.sum(cost) / labels.shape[0]

    def grad(self, logits, labels):
        neg_weight, pos_weight = self._weights
        grads = neg_weight * sigmoid(logits) - pos_weight * labels + \
                (pos_weight - neg_weight) * labels * sigmoid(logits)
        return grads / labels.shape[0]