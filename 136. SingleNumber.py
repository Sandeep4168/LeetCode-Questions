class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
              
        
        res = 0
        
        for n in nums:
            res = res ^ n
        return res
        
            
solution = Solution()

print(solution.singleNumber([4,1,2,1,2]))

