import numpy as np

def NMS(dets, conf_thresh, nms_thresh):
    '''
    dets:[x1,y1,x2,y2,score]
    conf_thresh:0.1
    nms_thresh:0.35
    '''
    dets = dets[dets[:,4] >= conf_thresh]
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    scores = dets[:, 4]
    areas = (x2-x1+1)*(y2-y1+1)
    order = np.argsort(scores)[::-1]
    keep = [] #返回对应的索引即可
    while order.size > 0:
        i = order[0]
        keep.append(i)
        if order.size == 1:
            break
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.maximum(x2[i], x2[order[1:]])
        yy2 = np.maximum(y2[i], y2[order[1:]])
        w = np.maximum(0, xx2-xx1+1)
        h = np.maximum(0, yy2-yy1+1)
        inter = w*h
        over = inter / (areas[i]+areas[order[1:]]-inter)
        inds = np.where(over<=nms_thresh)[0] #保留小的
        order = order[inds+1]
    return keep

if __name__ == "__main__":
    dets = np.array([[30, 20, 230, 200, 1], 
                     [50, 50, 260, 220, 0.6],
                     [210, 30, 420, 5, 0.7],
                     [430, 280, 460, 360, 0.8]])
    conf_thresh = 0.5
    num_thresh = 0.1
    keep_dets = NMS(dets, conf_thresh, num_thresh)
    print(keep_dets)
    print(dets[keep_dets])


    
    

  





