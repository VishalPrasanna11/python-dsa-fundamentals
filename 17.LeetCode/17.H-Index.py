class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        paper_count = [0] * (n+1)

        for c in citations:
            paper_count[min(n,c)] += 1
        
        h = n 

        papers = paper_count[n]

        while papers < h:
            h-= i
            papers+=paper_counts[h]

        return h
