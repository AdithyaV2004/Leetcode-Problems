class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        best = 1
        c=1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]:
                continue
            if nums[i] == nums[i - 1] + 1:
                c += 1
            else:
                best=max(best, c)
                c = 1
        best=max(best, c)
        return best
