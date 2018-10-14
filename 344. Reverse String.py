class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        #string is unmmutable, convert it to list
        s = list(s)
        head = 0 
        tail = len(s)-1
        while head<tail:
            s[head],s[tail] = s[tail],s[head]
            head+=1
            tail-=1
        #convert list back to string
        return ''.join(s)
solution  = Solution()
x  = solution.reverseString('hello')
print(x)


