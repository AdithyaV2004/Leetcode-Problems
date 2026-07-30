class Solution:
    def minimumPushes(self, word: str) -> int:
        l=len(word)
        n=l//8
        r=l%8
        c=0
        if n>0:
            for i in range(1, n+1):
                c+=i*8
        c+=(n+1)*r
        return (c)