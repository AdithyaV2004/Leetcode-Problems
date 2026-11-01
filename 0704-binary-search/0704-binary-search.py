class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)-1
        def bin_ser(lp, rp):
            if lp>rp:
                return -1
            mp=(lp+rp)//2
            if nums[mp]==target:
                return mp
            elif nums[mp]<target:
                return bin_ser(mp+1, rp)
            else:
                return bin_ser(lp, mp-1)
        return bin_ser(l, r)
