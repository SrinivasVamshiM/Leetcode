class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = 0
        for c in s:
            if c == '1':
                count += 1
        return ((count-1)*'1')+('0'*(len(s)-count))+'1'