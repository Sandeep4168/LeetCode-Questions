from xmlrpc.client import FastMarshaller


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        hashMap = {}
        flag = False

        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = i
            else:
                if abs(i - hashMap[nums[i]]) <= k:
                    flag = True
                hashMap[nums[i]] = i 

        return flag
    
solution = Solution()
    
testcase1= [1,2,3,1]
k1 = 3
testcase2 = [1,0,1,1]
k2  = 1
testcase3 = [1,2,3,1,2,3]
k3 = 2

print(solution.containsNearbyDuplicate(testcase3,k3))