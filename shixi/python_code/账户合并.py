from typing import List

#并查集
class UnionFind:
    def __init__(self, n):
        # 总数
        self.rank = [0]*n  # quick union优化（权重思想)
        self.size = n
        self.p = [i for i in range(n)]
    def find(self, x):
        # 查找根节点，即当前元素所属的集合
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])  # quick find 优化
        return self.p[x]
    def union(self, a, b):
        ar, br = self.find(a), self.find(b)
        # 两个元素位于同一个集合，跳过
        if ar == br:
            return
        # 不在同一个集合，合并
        else:
            ###优化的###
            if self.rank[ar] > self.rank[br]:
                self.p[br] = ar
            elif self.rank[ar] < self.rank[br]:
                self.p[ar] = br
            else:
                self.p[ar] = br
                self.rank[br] += 1
            self.size -= 1  # 每合并一次，size减一次
        
def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    res = []
    um = {} # 作用：存储每个邮箱属于哪个账户 格式：<邮箱，账户id>，同时 在遍历邮箱时，判断邮箱是否出现过 
    n = len(accounts)
    ds =  UnionFind(n)
    for i in range(n): 
        m = len(accounts[i])
        for j in range(1, m): #跳过用户名，从邮箱位置开始遍历
            s = accounts[i][j]
            if (s not in um.keys()):
                um[s] = i
            else :
                ds.union(i, um[s]) #合并属于同一个真正用户的id
            
    # 作用：存储每个账户下的邮箱 格式： <账户id, 邮箱列表> >
    # 注意：这里的key必须是账户id，不能是账户名称，名称可能相同，会造成覆盖
    umv = {}
    for k, v in um.items():
        if ds.find(v) in umv.keys():
            umv[ds.find(v)].append(k)
        else:
            umv[ds.find(v)] = [k]
    
    for k, v in umv.items():
        v.sort()
        temp = [accounts[k][0]]
        temp.extend(v)
        res.append(temp)
    return res

if __name__ == "__main__":
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
    print(accountsMerge(accounts))
