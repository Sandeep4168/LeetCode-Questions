class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
    
        """
        #Solution 1
        # nums_set = set(nums)
        
        # if(len(nums)== len(nums_set)):
        #     return False
        # return True
        
        # Solution 2
        
        temp = set()
        
        for n in nums:
            if n in temp:
                return True
            temp.add(n)
        return False
                
        
solution = Solution()

testCase1 = [1,2,3,1]
testCase2 = [1,2,3,4]
testCase3 = [1,1,1,3,3,4,3,2,4,2]
testCase4 = [3,1]

print(solution.containsDuplicate(testCase4))