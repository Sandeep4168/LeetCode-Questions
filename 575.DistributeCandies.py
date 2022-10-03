import math
class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        n = len(candyType)
        
        typesOfCandy = int(len(set(candyType)))
        
        if n == typesOfCandy:
            return n/2
        if n < typesOfCandy:
            return int(math.ceil(n/2))
        
        if n > typesOfCandy:
            if typesOfCandy > n/2:
                return int(n/2)
            else:
                return int(typesOfCandy)
        
solution = Solution()

# candyType = [1,1,2,2,3,3] #Output: 3
candyType = [1,1,2,3]  #Output: 2
candyType = [6,6,6,6]  #Output: 1


print(solution.distributeCandies(candyType))