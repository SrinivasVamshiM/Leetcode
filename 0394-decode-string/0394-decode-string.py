class Solution:
    def decodeString(self, s: str) -> str:
        
        num_stack = []
        str_stack = []
        strr = ""
        num = 0
        for char in s:
            if char.isdigit():
                num = num*10+int(char)
            elif char == '[':
                num_stack.append(num)
                str_stack.append(strr)
                num = 0
                strr = ""
            elif char == ']':
                n = num_stack.pop()
                strr = str_stack.pop() + strr*n
            else:
                strr += char
        return strr