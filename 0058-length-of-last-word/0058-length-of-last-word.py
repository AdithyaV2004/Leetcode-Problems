class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l=0
        for i in s.strip()[::-1]:
            if i==" ":
                break
            l+=1
        return l