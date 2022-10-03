class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        hashmap ={}
        count = 0
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1
        if len(hashmap) <= 1:
            return 0
        for key in hashmap:
            if key + 1 in hashmap:
                count = max(count, hashmap[key] + hashmap[key + 1])

        return count
        
        