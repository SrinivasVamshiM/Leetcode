class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        list1 = []
        
        list1 = [0] * (n + 1)  # Initialize list1 with zeros
        maxalt = list1[0]
        for i in range(n):
            list1[i+1] = list1[i] + gain[i]
            maxalt = max(maxalt, list1[i+1])
        return maxalt