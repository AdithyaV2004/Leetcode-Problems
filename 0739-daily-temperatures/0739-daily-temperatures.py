class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack=[]
        n=len(temp)
        res=[0]*n
        for i in range(n-1, -1, -1):
            if not stack:
                res[i]=0
            else:
                while stack and temp[stack[-1]]<=temp[i]:
                    stack.pop()
                if not stack:
                    res[i]=0
                else:
                    res[i]=stack[-1]-i
            stack.append(i)            
        return res