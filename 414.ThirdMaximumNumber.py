class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        temp = list(set(nums))
        
        return sorted(temp,reverse=True)[2] if len(temp) >= 3 else sorted(temp,reverse=True)[-1]
        
        
        
solution = Solution()
testcase1 = [3,2,1]
testcase2 = [1,2]
testcase3 = [2,2,3,1]

print(solution.thirdMax(testcase2))
                
                