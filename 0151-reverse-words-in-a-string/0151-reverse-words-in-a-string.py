class Solution:
    def reverseWords(self, s: str) -> str:
        words=[]
        i=len(s)-1
        while i>=0:
            while i>=0 and s[i]==" ":
                i-=1
            if i<0: break
            word=[]
            while i>=0 and s[i]!=" ":
                word.append(s[i])
                i-=1
            m=len(word)
            l, r=0, m-1
            while l<r:
                word[l], word[r]=word[r], word[l]
                l, r=l+1, r-1
            word=''.join(word)
            words.append(word)
        return " ".join(words)
