class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft=[]
        m=0
        for i in range(len(height)):
            maxLeft.append(m)
            m=max(m, height[i])
        maxRight=[0]*len(height)
        m=0
        for i in range(len(height)-1, -1, -1):
            maxRight[i]=m
            m=max(m, height[i])
        min_h=[]
        for i in range(len(height)):
            min_h.append(min(maxLeft[i], maxRight[i]))
        water=0
        for i in range(len(height)):
            qty=min_h[i]-height[i]
            if qty>=0:
                water+=qty
        return water
            