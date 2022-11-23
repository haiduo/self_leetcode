''' 
ref: https://borgwang.github.io/dl/2019/08/18/tinynn.html 
'''
import numpy as np

class Loss:
    def loss(self, *args, **kwargs):
        raise NotImplementedError

    def grad(self, *args, **kwargs):
        raise NotImplementedError

def log_softmax(x, t=1.0, axis=-1):
        x_ = x / t
        x_max = np.max(x_, axis=axis, keepdims=True)
        exps = np.exp(x_ - x_max) # https://kexue.fm/archives/6620
        exp_sum = np.sum(exps, axis=axis, keepdims=True)
        return x_ - x_max - np.log(exp_sum)

def softmax(x, t=1.0, axis=-1):
    x_ = x / t
    x_max = np.max(x_, axis=axis, keepdims=True)
    exps = np.exp(x_ - x_max)
    return exps / np.sum(exps, axis=axis, keepdims=True)

class SoftmaxCrossEntropy(Loss):

    def __init__(self, T=1.0, weights=None):
        self._weights = np.asarray(weights) if weights is not None else weights
        self._T = T

    def loss(self, logits, labels):
        nll = -(log_softmax(logits, t=self._T, axis=1) * labels).sum(axis=1)
        if self._weights is not None:
            nll *= self._weights[np.argmax(labels, axis=1)]
        return np.sum(nll) / labels.shape[0]

    def grad(self, logits, labels):
        grads = softmax(logits, t=self._T) - labels
        if self._weights is not None:
            grads *= self._weights
        return grads / labels.shape[0]


class CrossEntropyLoss(Loss):
    def loss(self, predicted, actual):
        m = predicted.shape[0]
        exps = np.exp(predicted - np.max(predicted, axis=1, keepdims=True))
        p = exps / np.sum(exps, axis=1, keepdims=True)
        nll = -np.log(np.sum(p * actual, axis=1))
        return np.sum(nll) / m

    def grad(self, predicted, actual):
        m = predicted.shape[0]
        grad = np.copy(predicted)
        grad -= actual
        return grad / m