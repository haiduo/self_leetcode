# python3
'''https://blog.csdn.net/gukedream/article/details/88050705'''
import numpy as np
 
def py_nms(dets, conf_thresh, num_thresh):
    """Pure Python NMS baseline."""
    #找出得分大于门限函数的框，在进行重合框筛选前就进行得分的筛选可以大幅度减少框的数量。
    dets = dets[dets[:,4] >= conf_thresh]

    #x1、y1、x2、y2、以及score赋值
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    scores = dets[:, 4]
 
    #每一个候选框的面积
    areas = (x2 - x1 + 1) * (y2 - y1 + 1) 
    #计算的是像素点个数，比如左上角和右下角像素点重合，此时面积应该是1而不是0，所以计算时要加1
    
    #order是按照score降序排序的
    order = np.argsort[::-1] #使用[::-1],可以建立scores.argsort()的逆序.返回索引值
    # order1 = list(scores)
    # order1.sort(key= None,reverse=True) #或者使用这个等价
 
    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)
        if order.size ==1:
            break 
        #计算当前概率最大矩形框与其他矩形框的相交框的坐标，会用到numpy的broadcast机制，得到的是向量
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])
 
        #计算相交框的面积,注意矩形框不相交时w或h算出来会是负数，用0代替
        w = np.maximum(0.0, xx2 - xx1 + 1)
        h = np.maximum(0.0, yy2 - yy1 + 1)
        inter = w * h
        #计算重叠度IOU：重叠面积/（面积1+面积2-重叠面积）
        ovr = inter / (areas[i] + areas[order[1:]] - inter)
 
        #找到重叠度不高于阈值的矩形框索引
        inds = np.where(ovr <= num_thresh)[0] 
        #np.where(condition, x, y)满足条件(condition)，输出x，不满足输出y。
        #只有条件 (condition)，没有x和y，则输出满足条件 (即非0) 元素的坐标 (等价于numpy.nonzero)。
        
        #将order序列更新，由于前面得到的矩形框索引要比矩形框在原order序列中的索引小1，所以要把这个1加回来
        order = order[inds + 1]
    return keep
 
# test
if __name__ == "__main__":
    dets = np.array([[30, 20, 230, 200, 1], 
                     [50, 50, 260, 220, 0.6],
                     [210, 30, 420, 5, 0.7],
                     [430, 280, 460, 360, 0.8]])
    conf_thresh = 0.5
    num_thresh = 0.1
    keep_dets = py_nms(dets, conf_thresh, num_thresh)
    print(keep_dets)
    print(dets[keep_dets])