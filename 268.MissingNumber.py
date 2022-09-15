class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        
        for i in range(len(nums)):
            res += (i - nums[i])
        return res



testCase1 = [3,0,1]

solution = Solution()

print(solution.missingNumber(testCase1))