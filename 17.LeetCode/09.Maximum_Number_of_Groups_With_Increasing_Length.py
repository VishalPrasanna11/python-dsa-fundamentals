class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        usageLimits.sort()

        total_usage = 0
        max_usage = 0
        for limit in usageLimits:
            total_usage += limit

            next_group_req = (max_usage+1)*(max_usage+2)//2

            if total_usage >= next_group_req:
                max_usage+=1

        
        return max_usage


        