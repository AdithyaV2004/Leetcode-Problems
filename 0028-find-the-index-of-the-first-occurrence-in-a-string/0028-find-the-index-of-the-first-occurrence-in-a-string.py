class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lp, rp=0, len(needle)
        while rp<=len(haystack):
            if haystack[lp:rp]==needle:
                return lp
            lp+=1
            rp+=1
        return -1
