class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        n = len(candies)
        print(m)
        list1 = [True if candies[i]+extraCandies >= m else False for i in range(n)]
        return list1