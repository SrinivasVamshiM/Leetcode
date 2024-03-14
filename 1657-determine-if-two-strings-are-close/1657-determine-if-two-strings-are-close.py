class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        dict1 = {}
        dict2= {}
        
        for char in word1:
            dict1[char] = dict1.get(char,0)+1
        for char in word2:
            dict2[char] = dict2.get(char,0)+1
        
        if set(dict1.keys()) != set(dict2.keys()):
            return False
        return sorted(dict1.values()) == sorted(dict2.values())