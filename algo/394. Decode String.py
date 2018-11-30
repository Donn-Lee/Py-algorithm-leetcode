
'''394. Decode String
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''

# 理解题目:
# 10[ab]2[cd] => 从左到右逐字处理即可
# 2[3[cd]] => 3[cd] 处理完, 会变成 2[ ]的内容, 得记住外层是什么

# 思路:
# 1. 从左到右逐字处理, 会先遇到外层 2[, 才遇到内层 3[ => 需要 stack 记住刚刚遇到的外层
# 2. 从左到右逐字处理, 得辨识数字, 和跨号里面的 string pattern

# 工作顺序:
# 1. 识别左跨号 [, 先抓数字:例如 2 和 10
# 2. 把数字存到 stack
# 2. 抓出 string pattern: 例如 ab, cd
# 4. 按右跨号 ] 出现时机, 处理 decode 操作


# 思路，用栈，因为内层的要decode 并且加到上一层去，栈可以告诉你上一层的pattern是什么
#创建list of list [[multipliers,pattern]] mutipliers是数字,pattern 是字母

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        #判断是否s是空或其他奇怪的东西
        if not s or len(s) == 0 :
            return ""
        #创建最外层的栈
        stack =[[0,""]]#最后所有被decode的string会一次添加到上一层，最终加到了stack[0][1]“”中
        #创建数字代表倍数:
        multiplier = ""
        #开始遍历
        for i in s:
            #若是数字，则加到multiplier中区
            if i.isdigit():
                multiplier+= i
            #若是‘['，这一层的数字将结束，但是我们还不知道字母是什么，暂且加一层[multipliers, ''],并将multiplier清零
            elif i == '[':
                stack.append([int(multiplier),""])
                multiplier = ""
            #如果碰到了字母，我们把字母加到最后一层的第二个元素中去
            elif i.isalpha():
                stack[-1][1] += i
            #如果碰到了']'，说明这一层结束，应该吧这一层 pop出来，decode，然后加到上一层的第二个元素（字母）中去
            elif i == ']':
                num, alpha = stack.pop()
                newalpha =  num * alpha
                #这是stack的-1层其实是原来的倒数第二层
                stack[-1][1] += newalpha
        #回到最外面一层
        return stack[0][1]

s = Solution()
print(s.decodeString('3[a]2[bc]'))
print(s.decodeString('3[a2[c]]'))









