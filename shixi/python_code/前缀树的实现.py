import collections

class Trie:
    def __init__(self):
        self.child = collections.defaultdict(dict) #等价self.child = {}  字典的实现方式
    
    def insert(self, word: str) -> None: #lc208题目答案
        nownode = self.child
        for s in word:
            if s not in nownode.keys():
                nownode[s] = collections.defaultdict(dict)  #创建下一个节点
            nownode = nownode[s]
        nownode['#']='#'         #有一定的局限性 前提是单词里不能有结束符
    
    def insert_c(self, word: str) -> None: #改编的前缀树,不保存中间的字符串
        nownode = self.child
        for s in word:
            if '#' in nownode.keys():
                nownode[s] = nownode.pop('#') #修改键(key)
                nownode[s] = collections.defaultdict(dict)
            elif s not in nownode.keys():
                nownode[s] = collections.defaultdict(dict)  #创建下一个节点
            nownode = nownode[s]
        if not nownode:
            nownode['#']='#'         #有一定的局限性 前提是单词里不能有结束符

    def search(self, word: str) -> bool:
        nownode = self.child
        for s in word:
            if s in nownode.keys():
                nownode = nownode[s]
            else:
                return False
        return '#' in nownode.keys()
        
    def startsWith(self, prefix: str) -> bool:
        nownode = self.child
        for s in prefix:
            if s in nownode.keys():
                nownode = nownode[s]
            else:
                return False
        return True
    
    def travel(self) -> list: #遍历前缀树
        nownode = self.child
        ret =[]
        str =''
        if not nownode:
            return ret
        def findkey(nownode, str):
            nonlocal ret
            if '#' in nownode: #如果当前字典的值的所有字典的关键字有结束符#，则输出
                return ret.append(str)
            for key in nownode:
                nodes = nownode[key]
                for node_s in nodes:
                    findkey({node_s:nodes[node_s]}, str+key)
        findkey(nownode, str)
        return ret

if __name__ == "__main__":
    words =  ["/a","/a/b","/a","/c/d","/c/d/e","/c/f"]
    obj = Trie()
    for word in words:
        # print(word)
        word = word if word else "''"
        obj.insert(word)
    for word in words:
        print('search %s: %s' % (word, obj.search(word)))
        print('startsWith %s: %s' % (word, obj.startsWith(word)))
    
    print(obj.travel())

    # del obj
    # obj = Trie()
    # print("\n")
    # for word in words:
    #     # print(word)
    #     word = word if word else "''"
    #     obj.insert_c(word)
    # for word in words:
    #     print('search %s: %s' % (word, obj.search(word)))
    #     print('startsWith %s: %s' % (word, obj.startsWith(word)))
