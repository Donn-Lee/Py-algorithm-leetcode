#brute force 
class Solution(object):
    
#bigO : O(n^3)

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        """
        def valid(s):
            return len(s) == len(set(s))

        longest = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if valid(s[i:j]):
                    longest =  max(longest,j-i)
        return longest

# s = Solution()
# l = s.lengthOfLongestSubstring('bbbbb')
# print(l)

class Solution2(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #greedy
        #l -- longest substring
        # if 'next character' in previous substring, we start from last same character +1 to 'next character'
        # abcdeb -> cdeb (b is next character and c is last same character + 1)
        # s[range(s)+1] raise error but s[range(s)+1:] won't 
        l, substring= 0, ""
        for i in range(len(s)):
            if substring.find(s[i]) == -1:
                
                substring += s[i]
                l = max(l,len(substring))
            else:
                print(substring)
                print(substring.find(s[i]))
                substring = substring[substring.find(s[i])+1:]+s[i]
                l = max(l,len(substring))
        return max(l,len(substring))


# s = Solution2()
# l = s.lengthOfLongestSubstring('bb')
# print(l)        


#if you are not confident about str.find 
class Solution3(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #start index where we should start.
        #map : use character as key and last index of character as value. 

        #if value large than the start means the character appeared once, adjust the start to last same 
        # character + 1

        # abcd + be : map =  {a:0,b:1,c:2,d:3} and start = 0(since a is start) and now we meet b which
        # value is 1 greater than 0 so that adjust start from a to c and now we have cdb + e and go on

        #here we just convert str.find to hashmap value comparing
        
        #l : longest line 

        l,map,start = 0,{},0
        for i in range(len(s)):
            start = max(start,map.get(s[i],-1) +1) # from abcd+b -> cd +b
            l = max(l, i - start +1) # original len(abcd) vs len(cdb)
            map[s[i]] = i #hashmap:character -> last index

        return l

# s = Solution3()
# l = s.lengthOfLongestSubstring('ab')
# print(l) 