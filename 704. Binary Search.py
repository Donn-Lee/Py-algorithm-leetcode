'''
Given a sorted (in ascending order) integer array nums of n elements and a target value, 
write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 '''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if (not nums) or  (len(nums) == 0):
            return -1
        head = 0
        tail = len(nums) -1
        while head <= tail:
            mid = (head + tail)//2
            if nums[mid]<target:
                head = mid +1
            elif nums[mid]>target:
                tail = mid - 1
            else:
                return mid
        return -1

nums = [-1,0,3,5,9,12]; target = 2
s = Solution()
print(s.search(nums,12))