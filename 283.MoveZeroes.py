class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        l = 0
        for n in range(len(nums)):
            if nums[n]:
                nums[l],nums[n] = nums[n],nums[l]
                l += 1
        return nums
    
    
        
        
        
        
        
        
    
solution = Solution() 
testcase = [0,1,0,3,12]
testcase1 = [0,0,1]



print(solution.moveZeroes(testcase1))
            
             
            