class Solution:
    @cache
    def f(self, nums, idx):
        if idx>=len(nums):
            return 0
        ans1=nums[idx]+self.f(nums, idx+2)
        ans2=self.f(nums, idx+1)
        return max(ans1, ans2)

    def rob(self, nums: List[int]) -> int:
        return self.f(tuple(nums), 0)