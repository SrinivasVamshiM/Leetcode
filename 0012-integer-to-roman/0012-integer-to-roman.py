class Solution:
    def intToRoman(self, num: int) -> str:
        roman_numerals = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        roman_numeral_string = ''
        for i in sorted(roman_numerals.keys(), reverse=True):
            while num >= i:
                roman_numeral_string += roman_numerals[i]
                num -= i
        return roman_numeral_string