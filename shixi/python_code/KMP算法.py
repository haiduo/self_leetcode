def build_next(patt):
    """计算Next数组"""
    next = [0]      # next数组(初值元素一个0)
    prefix_len= 0   #当前共同前后缀的长度,也表示前缀的最后一个字符位置
    i=1             #表示后缀的最后一个字符位置
    while i < len(patt):
        if patt[prefix_len]==patt[i]:
            prefix_len +=1
            next.append(prefix_len) 
            i += 1
        else:
            if prefix_len == 0:
                next.append (0)
                i += 1
            else: #借鉴KMP核心思想
                prefix_len = next[prefix_len-1]  #注意这里i不自增，仅是调整前缀的最后一个字符的下表位置
    return next

def kmp_search(string, patt):
    next = build_next(patt) #假设我们已经算出了next数组
    i=0 #主串中的指针
    j=0 #子串中的指针
    while i < len(string):
        if string[i] == patt[j]: #字符匹配,指针后移
            i += 1
            j+= 1
        elif j>0: #字符失配,根据next 跳过子串前面的一些字符  核心思想
            j= next[j - 1]
        else:#子串第一个字符就失配
            i += 1
        if j== len(patt):#匹配成功
            return i - j

if __name__ == "__main__":
    s = "ABABABCAA"
    t = 'ABA'
    t1 = 'ABC'
    print(kmp_search(s, t1))
