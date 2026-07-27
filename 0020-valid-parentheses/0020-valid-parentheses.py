class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        d={")":"(", "}":"{", "]":"["}
        for i in s:
            if i in d.values():
                st.append(i)
            else:
                if len(st)==0 or st.pop()!=d[i]:
                    return False
        return len(st)==0
                

        