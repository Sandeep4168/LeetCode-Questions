class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        
        for i in range(rowIndex):
            temp = [0] + res + [0]
            row =[]
            for j in range(len(temp) - 1):
                row.append(temp[j] + temp[j+1])
                res = row
        return res
    
solution = Solution()

print(solution.getRow(3))
                
            
        

        







