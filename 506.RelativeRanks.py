class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        
        scoreIndex = {s:i for i, s in enumerate(score)}
        
        scoreSorted = sorted(score,reverse=True)
        res = [0] * len(score)
        
        for i in range(len(scoreSorted)):
            if i == 0:
                res[scoreIndex[scoreSorted[i]]] = "Gold Medal"
            elif i == 1:
                res[scoreIndex[scoreSorted[i]]] = "Silver Medal"
            elif i == 2:
                res[scoreIndex[scoreSorted[i]]] = "Bronze Medal"
            else:
                res[scoreIndex[scoreSorted[i]]] = str(i+1)
        return res
                
                
                
                
