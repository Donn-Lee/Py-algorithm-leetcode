class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = {'a','e','i','o','u'}
        head = 0
        tail = len(s) - 1
        while head < tail:
            while head < tail and s[head] not in vowels:
                head += 1
            while head < tail and s[tail] not in vowels:
                tail -=1
            s[head],s[tail] = s[tail],s[head]
            head += 1
            tail -= 1

        return ''.join(s)

s = Solution()
print(s.reverseVowels('hello'))