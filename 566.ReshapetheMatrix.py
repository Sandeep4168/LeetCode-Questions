class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # matElements = []
        # for i in mat:
        #     for j in i:
        #         matElements.append(j)
        
        # rearrangedMat = []
        # if len(matElements ) != (r*c):
        #     return mat
        
        # a = 0
                
        # for i in range(r):
        #     rearrangedMat.append(matElements[a:a+c])
        #     a = a+c
        # return rearrangedMat
    
        flat = [item for sublist in mat for item in sublist]
        if r * c != len(flat): return mat    
        output = [flat[(row *c) :c * (row +1)] for row in range(r)]
        return output

solution = Solution()

# mat = [[1,2],[3,4]]
# r = 1
# c = 4 #output = [[1,2,3,4]]

mat = [[1,2],[3,4]]
r = 4
c = 1 #output = [[1],[2],[3],[4]]

print(solution.matrixReshape(mat,r,c))