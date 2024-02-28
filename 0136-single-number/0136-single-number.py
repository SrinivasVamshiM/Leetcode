class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        
        for i in nums:
            dict[i] = dict.get(i, 0) + 1
        for key,value in dict.items():
            if value == 1:
                return key