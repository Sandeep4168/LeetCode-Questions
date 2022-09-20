


from collections import Counter


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        temp = []
        
        c = Counter(nums1)
        
        for n in nums2:
            if c[n] >0:
                temp.append(n)
                c[n] -= 1
        return temp
                        
                        
        

solution = Solution()
# nums2 = [1,2,2,1]
# nums1 = [2,2]
# nums1 =[4,9,5]
# nums2 =[9,4,9,8,4]
nums2 = [1,2,2,1]
nums1 = [2]
print(solution.intersect(nums1,nums2))



