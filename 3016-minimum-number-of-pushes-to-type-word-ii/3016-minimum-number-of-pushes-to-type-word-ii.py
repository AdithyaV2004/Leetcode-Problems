class Solution:
    def minimumPushes(self, word: str) -> int:
        d={}
        for i in word:
            if i not in d:
                d[i]=0
            d[i]+=1
        f=sorted(d.values())[::-1]
        l=len(f)
        rl=[]
        c=0
        print(f)
        for i in range(l):
            c+=f[i]
            if i%8==7:
                rl.append(c)
                c=0
        rl.append(c)
        print(rl)
        c=0
        for i in range(len(rl)):
            c+=(i+1)*rl[i]
        return c

