'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
#思路：遍历整个string，若出现了一个新的右括号，最近也应该能pop出一个相同的左括号（stack）
#方法，两个set，分别存储，{'(','{','{'}和{'()','{}','[]'}，每次有一个左括号时存储在list中等待pop
#检查三个问题，新出现的右括号应该和左括号相同；新出现右括号时，存储左括号的list应该长度不为零；检查完以后，左括号list长度应该为0
        left = set(('{','(','['))
        match = set(('[]','{}','()'))
        stack = list()
        if len(s) == 0:
            return True
        for i in s:
            if i in left:
                stack.append(i)
            else:
            #新出现右括号时，存储左括号的list应该长度不为零
                if len(stack) == 0:
                    return False
                else:
                    left_pop = stack.pop()
            #新出现的右括号应该和左括号相同
                    if left_pop+i not in match:
                        return False
        #检查完以后，左括号list长度应该为0
        return len(stack)== 0 

s = Solution()
print(s.isValid(']'))










