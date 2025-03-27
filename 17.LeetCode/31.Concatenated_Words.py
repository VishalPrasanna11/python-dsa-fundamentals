class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # Sort by word length (shortest first)
        words.sort(key=len)
        
        wordSet = set()
        dp = {}
        
        def dfs(word):
            if word in dp:
                return dp[word]
            
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if ((prefix in wordSet and suffix in wordSet)
                 or (prefix in wordSet and dfs(suffix))):
                    dp[word] = True
                    return dp[word]
            dp[word] = False
            return dp[word]

        res = []

        for w in words:
            # Skip empty words
            if not w:
                continue
                
            # Check if current word can be formed by concatenating other words
            if dfs(w):
                res.append(w)
                
            # Add word to set after checking
            wordSet.add(w)
            
        return res