from typing import List

class Expression(set): #构建一个集合类
    def __add__(self, other):
        ans = Expression()
        for elem in self:
            ans.add(elem)
        for elem in other:
            ans.add(elem)
        return ans

    def __mul__(self, other):
        ans = Expression()
        for elem1 in self:
            for elem2 in other:
                ans.add(elem1 + elem2)
        return ans

class Solution:
    def braceExpansionII1(self, expression: str) -> List[str]:
        stack = [[Expression()]] #构造栈
        for ch in expression:
            if ch.isalpha():
                if not stack[-1][-1]:
                    stack[-1][-1] = Expression((ch,))
                else:
                    stack[-1][-1] = stack[-1][-1] * Expression((ch,))
            else:
                if ch == "{":
                    stack.append([Expression()])
                elif ch == ",":
                    stack[-1].append(Expression())
                elif ch == "}":
                    now_exp = Expression()
                    for exp in stack.pop():
                        now_exp = now_exp + exp
                    if not stack[-1][-1]:
                        stack[-1][-1] = now_exp
                    else:
                        stack[-1][-1] = stack[-1][-1] * now_exp
            # print(ch, "->", stack)
        return sorted(list(stack[0][0]))

    def braceExpansionII2(self, expression): #简化版
        s = [{''}]
        for c in expression:
            if c==',': s[-2:] = [s[-2] | s[-1], {''}]
            elif c=='}': s[-1] = set(pre+suf for suf in (s.pop() | s.pop()) for pre in s[-1] )
            elif c=='{': s += [set(), {''}]
            else: s[-1] = set(pre+c for pre in s[-1])
        return sorted(s[-1])

    def braceExpansionII3(self, expression: str) -> List[str]:
        ''' "{a,b}{c,{d,e}}" or "{{a,z},a{b,c},{ab,z}}"
        使用压栈来存储当前括号的状态，如果遇到新的左括号，将当前确定和未确定的元素集合保存起来。
        当遇到右括号，将当前所有未确定加入确定中，并出栈，将确定加入到上一层的未确定中（相乘）。
        '''
        stack = [set(), {''}]
        for c in expression:
            if c == '{':
                stack.append(set()) # 压入 当前层已经确定元素集合
                stack.append({''}) # 压入 当前层未确定元素集合
            elif c == '}':
                unknow = stack.pop() # 出栈
                know = stack.pop() | unknow # 合并两个集合，由于遇见}，未确定的集合可以并入到已确定集合中
                stack[-1] = {i+j for i in stack[-1] for j in know} # 将当前层与上一层未确定元素相×，完成出栈
            elif c == ',':
                # 未确定元素可以确定结束
                stack[-2] = stack[-1] | stack[-2] # 将未确定元素加入确定元素集合中
                stack[-1] = {''} # 未确定元素清0
            else:
                # 输入的为字母，直接与未确定元素集合×上当前字母
                stack[-1] = {i+c for i in stack[-1]}
        return sorted(list(stack[-1]|stack[-2]))


if __name__ == "__main__":
    sol = Solution()
    expression = "{a,b}{c,{d,e}}"
    print(sol.braceExpansionII1(expression)) #["ac","ad","ae","bc","bd","be"]
    print(sol.braceExpansionII2(expression)) #["ac","ad","ae","bc","bd","be"]
    print(sol.braceExpansionII3(expression)) #["ac","ad","ae","bc","bd","be"]
    expression = "{{a,z},a{b,c},{ab,z}}"
    print(sol.braceExpansionII1(expression)) #["a","ab","ac","z"]
    print(sol.braceExpansionII2(expression)) #["a","ab","ac","z"]
    print(sol.braceExpansionII3(expression)) #["a","ab","ac","z"]