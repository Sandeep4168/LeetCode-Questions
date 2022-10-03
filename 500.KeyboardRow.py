import re

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        output=[]
        for i in words :
            if re.match("^[qwertyui]+$", i.lower()) or re.match("^[asdfghjkl]+$",i.lower()) or re.match("^[zxcvbnm]+$", i.lower()) :
                output.append(i)
        return output
        
                  
    
    
solution = Solution()
words = ["Hello","Alaska","Dad","Peace"]


print(solution.findWords(words))