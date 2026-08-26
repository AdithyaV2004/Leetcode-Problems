class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r=0, 0
        maxlen=0
        d={}
        while r<len(s):
            if s[r] not in d:
                d[s[r]]=0
            d[s[r]]+=1
            maxfreq=0
            for i in d:
                maxfreq=max(maxfreq,d[i])
            if ((r-l+1)-maxfreq)>k:
                d[s[l]]-=1
                l+=1
            else: maxlen=max(maxlen, r-l+1)
            r+=1
        return maxlen