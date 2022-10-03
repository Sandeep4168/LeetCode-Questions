class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # O(n ^ 2)
        res = []
        
        # def greatestElement(n,nums):
        #     if len(nums) == 0:
        #         return -1
        #     for i in range(len(nums)):
        #         if nums[i] > n:
        #             return nums[i]
        #     return -1
       
        
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         if nums1[i] == nums2[j]:
        #             if nums1[i] < greatestElement(nums2[j],nums2[j+1:]):
        #                 res.append(greatestElement(nums2[j],nums2[j+1:]))
        #             else:
        #                 res.append(-1)
        # return res
    
        # O(m + n)
        
        numsIdx = {n : i for i , n in enumerate(nums1)}
        
        res = [-1] * len(nums1)
        
        stack = []
        
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = numsIdx[val]
                res[idx] = cur
            if cur in numsIdx:
                stack.append(cur)
        return res
                
        
    
    

                    
                    
                    
    
# nums1 = [4,1,2] # 1 ,2, 4
# nums2 = [1,3,4,2] # 1, 2, 3 , 4

# nums1 = [2,4]
# nums2 = [1,2,3,4] # output =[3,-1]

nums1 =[1,3,5,2,4]
nums2 =[6,5,4,3,2,1,7] #[7,7,7,7,7]

solution = Solution()

print(solution.nextGreaterElement(nums1,nums2))