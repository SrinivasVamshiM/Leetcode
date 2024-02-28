class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or not s:
            return s
        list1 = ['']*numRows
        
        current = 0
        direction = 1
        
        for c in s:
            list1[current]+=c
            current += direction
            if current == 0 or current == numRows-1:
                direction *= -1
        return ''.join(list1)