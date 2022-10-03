class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l , output = 0, 0
        
        for r, n in enumerate(nums):
            if n == 0:
                l = r + 1
            output = max(output,r-l+1)
        return output




nums = [1,1,0,1,1,1]

solution = Solution()

print(solution.findMaxConsecutiveOnes(nums))