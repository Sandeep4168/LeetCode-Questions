class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # tempdict = {}
        
        # res, maxCount = 0, 0
        
        # for n in nums:
        #     tempdict[n] = 1 + tempdict.get(n,0)
        #     res = n if tempdict[n] > maxCount else res
        #     maxCount = max(tempdict[n],maxCount)
        # return res
        
        res, count = 0, 0
        
        for n in nums:
            if count == 0:
                res = n
            count += (1 if res == n else -1)
        return res
        
     
            
testCase1 = [2,2,1,1,1,2,2]

solution = Solution()

print(solution.majorityElement(testCase1))