class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        l=[]
        nums.sort()
        n=len(nums)
        for i, j in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue
            lp, rp=i+1, n-1
            while lp<rp:
                s=j+nums[lp]+nums[rp]
                if s>0:
                    rp-=1
                elif s<0:
                    lp+=1
                else:
                    l.append([j, nums[lp], nums[rp]])
                    lp+=1
                    while lp<rp and nums[lp]==nums[lp-1]:
                        lp+=1
        return l