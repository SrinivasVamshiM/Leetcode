class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict1 = {}
        
        for i in arr:
            dict1[i] = dict1.get(i,0)+1
        x = dict1.values()
        return len(x) == len(set(x))