from typing import List
from collections import defaultdict
from collections import deque

#广度度优先搜索
def canFinish1(numCourses: int, prerequisites: List[List[int]]) -> bool:
    in_degree_list = [0] * numCourses #入度数组(列表，保存所有课程的依赖课程总数)
    relation_dict = defaultdict(list) #关系表(字典，保存所有课程与依赖课程的关系)
    for i in prerequisites:
        in_degree_list[i[0]] += 1 #保存课程初始入度值
        relation_dict[i[1]].append(i[0]) # 添加依赖它的后续课程
    queue = deque()
    for i in range(len(in_degree_list)):
        if in_degree_list[i] == 0: #入度为0的课程入列
            queue.append(i) #队列只存储入度为0的课程，也就是可以直接选修的课程
    while queue:
        current = queue.popleft()
        numCourses -= 1 #选修课程-1
        relation_list = relation_dict[current]
        if relation_list: #如果有依赖此课程的后续课程则更新入度
            for i in relation_list:
                in_degree_list[i] -= 1
                if in_degree_list[i] == 0: #后续课程除去当前课程无其他依赖课程则丢入队列
                    queue.append(i)
    return numCourses == 0

def canFinish1_2(numCourses: int, prerequisites: List[List[int]]) -> bool:
    in_degree_list = [0] * numCourses #入度数组(列表，保存所有课程的依赖课程总数)
    relation_dict = defaultdict(list) #关系表(字典，保存所有课程与依赖课程的关系)
    result = list()
    for i in prerequisites:
        in_degree_list[i[0]] += 1 #保存课程初始入度值
        relation_dict[i[1]].append(i[0]) # 添加依赖它的后续课程
    queue = deque()
    for i in range(len(in_degree_list)):
        if in_degree_list[i] == 0: #入度为0的课程入列
            queue.append(i) #队列只存储入度为0的课程，也就是可以直接选修的课程
    while queue:
        current = queue.popleft()
        result.append(current)
        relation_list = relation_dict[current]
        if relation_list: #如果有依赖此课程的后续课程则更新入度
            for i in relation_list:
                in_degree_list[i] -= 1
                if in_degree_list[i] == 0: #后续课程除去当前课程无其他依赖课程则丢入队列
                    queue.append(i)
    if len(result) != numCourses:
        return []
    return result

#深度优先搜索
def canFinish2(numCourses: int, prerequisites: List[List[int]]) -> bool:
    relation_dict = defaultdict(list) #关系表(字典，保存所有课程与依赖课程的关系)
    visited = [0]*numCourses #标记每个节点的状态:0=未搜索,1=搜索中, 2=已完成
    result = 0
    invalid = False #判断有向图中是否有环
    for i in prerequisites:
        relation_dict[i[1]].append(i[0]) # 添加依赖它的后续课程
    def dfs(u: int): 
        nonlocal invalid
        nonlocal result
        visited[u] = 1
        for v in relation_dict[u]:
            if visited[v] == 0:
                dfs(v)
                if invalid:
                    return
            elif visited[v] == 1:
                invalid = True
                return
        visited[u] = 2
        result += 1
    for i in range(numCourses):
        if not invalid and not visited[i]:
            dfs(i)
    return result == numCourses

def canFinish2_2(numCourses: int, prerequisites: List[List[int]]) -> bool:
    relation_dict = defaultdict(list) #关系表(字典，保存所有课程与依赖课程的关系)
    visited = [0]*numCourses #标记每个节点的状态:0=未搜索,1=搜索中, 2=已完成
    result = list()
    invalid = False #判断有向图中是否有环
    for i in prerequisites:
        relation_dict[i[1]].append(i[0]) # 添加依赖它的后续课程
    def dfs(u: int): 
        nonlocal invalid
        nonlocal result
        visited[u] = 1
        for v in relation_dict[u]:
            if visited[v] == 0:
                dfs(v)
                if invalid:
                    return
            elif visited[v] == 1:
                invalid = True
                return
        visited[u] = 2
        result.append(u)
    for i in range(numCourses):
        if not invalid and not visited[i]:
            dfs(i)
    if invalid:
        return []
    return result[::-1]


if __name__ == "__main__":
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print(canFinish1(numCourses, prerequisites))
    print(canFinish1_2(numCourses, prerequisites))
    print(canFinish2(numCourses, prerequisites))
    print(canFinish2_2(numCourses, prerequisites))