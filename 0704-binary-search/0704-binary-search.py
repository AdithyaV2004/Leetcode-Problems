class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lp, rp = 0, len(nums)-1
        while lp<=rp:
            mp=(lp+rp)//2
            if nums[mp]==target:
                return mp
            elif nums[mp]<target:
                lp=mp+1
            else:
                rp=mp-1
        return -1
