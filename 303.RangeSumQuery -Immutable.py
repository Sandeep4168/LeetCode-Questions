class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.lst = []
        sum_ = 0
        for i in nums:
            sum_ += i
            self.lst.append(sum_)
    

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left > 0 and right >0:
            return self.lst[right] - self.lst[left-1]
        else:
            return self.lst[right]
        
            
            
            
# numArray = NumArray([-4,-5])  
numArray = NumArray([-2,0,3,-5,2,-1])

#print(numArray.sumRange(0, 2)) # return (-2) + 0 + 3 = 1     
# print(numArray.sumRange(1, 1)) # return 3 + (-5) + 2 + (-1) = -1  
print(numArray.sumRange(0, 5)) # return 3 + (-5) + 2 + (-1) = -1  
# print(numArray.sumRange(0, 0)) # return 3 + (-5) + 2 + (-1) = -1  

    