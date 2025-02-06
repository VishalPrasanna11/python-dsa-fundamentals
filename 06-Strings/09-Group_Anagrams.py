#Group AnaGrams
#Given a list of strings, group anagrams together.

#Example:
#Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
#Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]


def groupAnagrams(strs):
    # Write your code here.
    anagrams = {}
    
    for string in strs:
        sorted_string = "".join(sorted(string))
        
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]
            
    return list(anagrams.values())

#Time Complexity: O(n*mlogm)
#Space Complexity: O(n*m)

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) #[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
print(groupAnagrams(["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"])) #[['cab'], ['tin'], ['pew'], ['duh'], ['may'], ['ill'], ['buy'], ['bar'], ['max'], ['doc']]
print(groupAnagrams(["ca", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"])) #[['ca'], ['tin'], ['pew'], ['duh'], ['may'], ['ill'], ['buy'], ['bar'], ['max'], ['doc']]
