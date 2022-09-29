
def isVaild(s: str) -> bool:
    # # 不包含其他字符的话
    # if len(s) % 2 == 1:
    #         return False
    #定义栈
    stk = []
    # 括号字符列表
    chars_ = ['(', ')', '{', '}', '[', ']']
    #括号匹配对
    pair = {')':'(', '}':'{', ']':'['}
    #遍历整个字符串
    for char_ in s:
        # 去除“其他字符”
        if char_ not in chars_: continue
        # 右括号：栈为空或栈顶元素不匹配则返回False， 否则弹出栈顶元素
        if char_ in pair:
            if not stk or stk[-1] != pair[char_]: return False
            stk.pop()
        else:
            # 将左括号压入栈
            stk.append(char_)
    # 左右括号如果全部是匹配的那么此时栈应该是空的
    # 栈为空返回True 不为空返回False：
    return not stk

if __name__ == '__main__':
    arr = "s(sd)[sds]"
    print(isVaild(arr))
    arr = "" #默认匹配
    print(isVaild(arr))