class Solution:
    def reverseWords(self, s: str) -> str:
        ss=s.strip().split()
        res=""
        for i in ss:
            res=i+" "+res
        return res.rstrip()