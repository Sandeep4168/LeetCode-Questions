class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        
        g = sorted(g)
        s = sorted(s)
        
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
                j += 1
            else:
                j += 1
        return i            
            
                    
                
                
            
            
        




g = [1,2,3]
s = [1,1]

# g = [1,2]
# s = [1,2,3]  #ans = 2

# g = [10,9,8,7]
# s = [5,6,7,8]   # ans = 2
solution = Solution()

print(solution.findContentChildren(g,s))

