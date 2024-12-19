#Group Anagrams
#LeeCode: https://leetcode.com/problems/group-anagrams/

#Problem:
#Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#Example 1:
#Input: strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))

            if sorted_s not in group_anagrams:
                group_anagrams[sorted_s] = []

            group_anagrams[sorted_s].append(s)

        return list(group_anagrams.values())


#Test the solution
s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # [["bat"],["nat","tan"],["ate","eat","tea"]]
print(s.groupAnagrams([""])) # [[""]]
print(s.groupAnagrams(["a"])) # [["a"]]
print(s.groupAnagrams(["",""])) # [["",""]]
print(s.groupAnagrams(["a","b"])) # [["a"],["b"]]
print(s.groupAnagrams(["a","b","c"])) # [["a"],["b"],["c"]]
print(s.groupAnagrams(["a","b","c","d"])) # [["a"],["b"],["c"],["d"]]
print(s.groupAnagrams(["a","b","c","d","e"])) # [["a"],["b"],["c"],["d"],["e"]]
print(s.groupAnagrams(["a","b","c","d","e","f"])) # [["a"],["b"],["c"],["d"],["e"],["f"]]

#Time Complexity: O(n*mlogm)
#Space Complexity: O(n*m)


        