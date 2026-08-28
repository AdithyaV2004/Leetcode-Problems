class Solution:
    def tot_hrs(self, piles, m):
        hrs=0
        for i in piles:
            hrs+=math.ceil(i/m)
        return hrs
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high=1, max(piles)
        while low<high:
            mid=(low+high)//2
            if self.tot_hrs(piles, mid)<=h:
                high=mid
            else:
                low=mid+1
        return low
        