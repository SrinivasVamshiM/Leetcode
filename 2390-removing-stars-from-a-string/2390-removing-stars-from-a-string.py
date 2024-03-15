class Solution:
    def removeStars(self, s: str) -> str:
        x = s.count("*")
        n = len(s)
        ans = []
        if x == 0:
            return s
        for i in range(n):
            if s[i] == "*" and ans:
                ans.pop()
                continue
            else:
                ans.append(s[i])
        return "".join(ans)
    
                