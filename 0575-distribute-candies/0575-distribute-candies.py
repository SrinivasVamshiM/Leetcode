class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        canEat = n//2
        dict1 = {}
        for i in candyType:
            dict1[i] = dict1.get(i,0)+1
        m = len(dict1)
        
        return min(canEat,m)