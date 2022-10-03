class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        padZeroes = [[0] * len(grid[0])]
        newGrid = padZeroes + grid + padZeroes
        for i in range(len(newGrid)):
            newGrid[i] = [0] + newGrid[i] + [0]
            
        per = 0
        
        print(newGrid)
        
        
        for i in range(len(newGrid)):
            for j in range(len(newGrid[i])):
                if newGrid[i][j] == 1:
                    if newGrid[i][j+1] == 0:
                        per += 1
                    if newGrid[i+1][j] == 0:
                        per += 1
                    if newGrid[i-1][j] == 0:
                        per += 1
                    if newGrid[i][j-1 ] == 0:
                        per += 1
        return per
                        
                        
        
       
        
        
        
# grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

grid = [[0,0,1]]
        
solution = Solution()

solution.islandPerimeter(grid)