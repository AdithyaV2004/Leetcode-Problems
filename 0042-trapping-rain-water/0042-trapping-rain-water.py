class Solution:
    def trap(self, height: List[int]) -> int:
        lp, rp=0, len(height)-1
        maxL=height[lp]
        maxR=height[rp]
        amt=0
        while lp<rp:
            if maxL<=maxR:
                lp+=1
                maxL=max(maxL, height[lp])
                amt+=maxL-height[lp]
            else:
                rp-=1
                maxR=max(maxR, height[rp])
                amt+=maxR-height[rp]
        return amt