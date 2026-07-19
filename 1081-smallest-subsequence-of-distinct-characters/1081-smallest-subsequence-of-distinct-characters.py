class Solution:
    def smallestSubsequence(self, s: str) -> str:
        d={}
        for i in range(len(s)):
            d[s[i]]=i
        st=[s[0]]
        oc=set(st)
        for i in range(1, len(s)):
            if s[i] in oc:
                continue
            if len(st)>0 and s[i]<st[-1]:
                while len(st)>0:
                    if st[-1]>s[i] and d[st[-1]]>i:
                        ch=st.pop()
                        oc.remove(ch)
                    else:
                        break
            st.append(s[i])
            oc.add(s[i])
        return "".join(st)

            