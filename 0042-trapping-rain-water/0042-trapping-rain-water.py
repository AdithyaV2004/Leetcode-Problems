class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        lp, rp=0, n-1
        maxL=height[lp]
        maxR=height[rp]
        amt=0
        while lp<rp:
            if maxL<=maxR:
                lp+=1
                qty=maxL-height[lp]
                if qty>0:
                    amt+=qty
                maxL=max(maxL, height[lp])
            else:
                rp-=1
                qty=maxR-height[rp]
                if qty>0:
                    amt+=qty
                maxR=max(maxR, height[rp])
            print(lp-1, maxL, rp, maxR, amt)
        return amt