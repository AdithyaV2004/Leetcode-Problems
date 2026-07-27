class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        fp=[1]*l
        bp=[1]*l
        for i in range(1, l):
            fp[i]=fp[i-1]*nums[i-1]
        for i in range(l-2, -1, -1):
            bp[i]=bp[i+1]*nums[i+1]
        for i in range(l):
            nums[i]=bp[i]*fp[i]
        return nums

