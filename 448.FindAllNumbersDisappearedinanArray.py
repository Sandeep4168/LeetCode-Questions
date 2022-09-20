class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Mark the numbers to negative
        
        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])
            
        res = []
        
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res