import numpy as np

from loss import SoftmaxCrossEntropy, softmax

# define net
class OneLayerNetwork():
    def __init__(self, dimension, num_classes):
        self.layers = dimension
        self.num_classes = num_classes
        self.w = self.generate_wt(self.layers, self.num_classes)
        self._is_training = True
    
    # initializing the weights randomly
    def generate_wt(self, x, y):
        l =[]
        for i in range(x * y):
            l.append(np.random.randn())
        return(np.array(l).reshape(x, y))
    
    @property
    def is_training(self):
        return self._is_training

    def compute_logits(self, data):
        # net layer
        z = data.dot(self.w)# input of out layer
        # output = sigmoid(z)# output of out layer
        return(z)

iteration = 10
batch_size = 20
dimension = 100
num_classes = 10
# generate data and label
data = np.random.random([iteration, batch_size, dimension])  # 20 sets of data with dimension 100
labels = np.random.randint(num_classes, size=[iteration, batch_size])  # labels are 0~9

# init net
network = OneLayerNetwork(dimension, num_classes)
compute_loss = SoftmaxCrossEntropy()


def compute_accuracy(prediction, labels):
    # max_idex
    test_pred_idx = np.argmax(prediction, axis=-1)
    test_y_idx = labels
    total_num = len(test_pred_idx) if test_pred_idx.ndim > 1 else test_pred_idx.size
    hit_num = int(np.sum(test_pred_idx == test_y_idx))
    accuracy = 1.0 * hit_num / total_num
    network._is_training = True
    return accuracy

def compute_prediction(data):
    network._is_training = False
    score = network.compute_logits(data)
    logits = softmax(score)
    return logits


def main():
    epoch = 100
    lr = 0.001
    for j in range(epoch):
        for i in range(len(data)):
            logits = network.compute_logits(data[i])  # output of the network with shape[20, 10]
            loss = compute_loss.loss(logits, labels[i])  # compute cross-entropy loss
            # print(f"loss: {loss}")
            d_grad =  compute_loss.grad(logits, labels[i])
            # Updating parameters
            if d_grad.ndim > 1:
                u_grad = data[i].transpose().dot(d_grad)
            else:
                u_grad = np.expand_dims(data[i].transpose(), axis=1).dot(np.expand_dims(d_grad, axis=0)) 
            network.w = network.w-(lr*(u_grad))
            # print(f"w_L2_norm: {np.linalg.norm(network.w)}")

            prediction = compute_prediction(data[i])  # prediction made by the model
            accuracy = compute_accuracy(prediction, labels[i])  # compute accuracy of the batch
            print(f"loss: {loss}, accuracy: {accuracy}")

# KP0: Create a class OneLayerNetwork with __init__ to save parameters, and compute_logits
# KP1: Write compute_loss, compute_prediction, compute_accuracy correctly

if __name__ == "__main__":
    main()