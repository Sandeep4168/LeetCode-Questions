"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
"""
import math
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        low = 0
        high = len(nums) - 1
        mid = math.floor((low + high) / 2)
        
        while nums[mid] != target and low <= high:
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            mid = math.floor((low + high) / 2) 
        if nums[mid] == target:
            return mid
        else:
            return high + 1
        
solution = Solution()

#print(solution.searchInsert([1,3,5,6],5))
print(solution.searchInsert([1,3,5,6],2))
        
        
        