class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        d = {}
        for i in s:
            if i not in d:
                d[i]=0
            d[i]+=1
        max_freq = max(d.values())
        if max_freq > (n + 1) // 2:
            return ""
        l = [""] * n
        chars = sorted(d.items(), key=lambda x: -x[1])
        p = 0
        for char, count in chars:
            for _ in range(count):
                if p >= n:
                    p = 1 
                if l[p] != "":
                    return "" 
                l[p] = char
                p += 2
        return "".join(l)
