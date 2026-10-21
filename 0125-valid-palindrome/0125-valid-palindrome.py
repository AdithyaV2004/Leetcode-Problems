class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[]
        for i in s:
            if i.isalnum():
                l.append(i.lower())
        v=l[:]
        lp, rp=0, len(l)-1
        while lp<rp:
            v[lp],v[rp]=l[rp], l[lp]
            lp, rp=lp+1,rp-1
        print(l, v)
        return v==l