class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        result = ""
        len1 = len(str1)
        len2 = len(str2)
        def isDivisor(l):
            if len1%l or len2%l:
                return False
            f1 = len1//l
            f2 = len2//l
            return (str1[:l]*f1 == str1 and str1[:l]*f2 == str2)
        for l in range(min(len1,len2), 0, -1):
            if isDivisor(l):
                return str2[:l]
        return result
#ikkada first manam for loop lo two strings lo smallest tesukoni reverse lo traverse chesi is Divisor function lo len check chesam. f1, f2 create chesi uppudu f1 and f2 times str1 and str2 substr multiple chesta same str1 and str2 full undali, unta return true. Then return substr of [:l]
