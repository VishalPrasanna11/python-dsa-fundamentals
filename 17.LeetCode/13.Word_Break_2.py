class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        # wordDict = set(wordDict)
        # def backtrack(i):
        #     if i == len(s):
        #         res.append(" ".join(cur))
        #         return
  
        #     for j in range(i,len(s)):
        #         w = s[i:j+1]
        #         if w in wordDict:
        #             cur.append(w)
        #             backtrack(j+1)
        #             cur.pop()

        # cur = []
        # res = []
        # backtrack(0)
        # return res
        wordDict = set(wordDict)
        cache = {}

        def backtrack(i):
            if i == len(s):
                return [""]
            
            res = []

            for j in range(i,len(s)):
                w = s [i:j+1]
                if w not in wordDict:
                    continue
                strings = backtrack(j + 1)
                if not strings:
                    continue
                for substr in strings:
                    sentence = w
                    if substr: 
                        sentence += " " + substr
                    res.append(sentence)
            cache[i]= res
            return res
            
        return backtrack(0)
        