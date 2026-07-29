from math import comb
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n=len(s)
        mid=n//2
        freq=[0]*26
        for i in range(mid):
            freq[ord(s[i])-ord('a')]+=1
        def perm(rem):
            acc=1
            for ci in range(26):
                f=freq[ci]
                if not f: continue
                if f>rem: return 0
                acc*=math.comb(rem,f)
                if acc>k:return acc
                rem-=f
            return acc
        left=[]
        start=0
        for i in range(mid):
            selected=False
            for ci in range(26):
                if not freq[ci]: continue
                freq[ci]-=1
                p=perm(mid-i-1)
                if start+p>=k:
                    left.append(chr(ci+ord('a')))
                    selected=True
                    break
                freq[ci]+=1
                start+=p
            if not selected: return ""            
        mid=s[n//2] if n%2!=0 else ''
        print(left)
        return "".join(left)+mid+"".join(left[::-1])

