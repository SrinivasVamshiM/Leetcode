class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -(2**31) and divisor == -1:
            return (2**31-1)
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quot = 0
        while dividend >= divisor:
            temp = divisor
            multiple = 1           
            while dividend >= temp<<1:
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            quot += multiple
        return min(max(-2**31, sign*quot), 2**31-1)
            

            