import numpy as np
import random
import math

def random_point(num_of_points, radius):
    points = []
    for i in range(0, num_of_points):
        # 因为x,y可能取到[1,1]或者[-1,-1]之类的，所以得需要先用极坐标系生成，再转笛卡尔坐标系计算
        theta = random.random() * 2 * np.pi #极坐标的θ
        r = random.random() * radius  #极坐标的r
        x = math.cos(theta) * (r ** 0.5)  # 极坐标系 转 笛卡尔坐标系 r = 根号下( (cosθ√r)**2 + (sinθ√r)**2)
        y = math.sin(theta) * (r ** 0.5)
        points.append([x,y])
    return points

def main():
    num_of_points = 10000
    points = random_point(num_of_points, 1)
    res =0
    for i in points:
        res += (i[0] ** 2 + i[1] ** 2) ** 0.5  # 距离d=根号下(x²+y²)
    print(res / num_of_points)

if __name__ == '__main__':
    main()

    # random.random()  # 随机生成 [0.0, 1.0) 的浮点数
    # random.randint(1, 10)  #随即生成 [1, 10] 的整数
    # random.randrange(1, 10)  #随即生成 [1, 10) 的整数
    # random.uniform(1, 10)  #随即生成 [1.0, 10.0) 的浮点数
    # a = ['a', 'b', 'c', 'd', 'e']
    # print(random.choice(a))  #随机选择一个元素 返回元素值
    # print(random.choices(a, [1,1,2,3,5]))  #随机按权重选择一个元素 返回列表
    # print(random.choices(a, cum_weights=[1,1,2,3,5], k=2))  #随机选择k个元素 返回列表
    # print(random.sample(a, k=2))  #随机选择k个元素 返回列表


