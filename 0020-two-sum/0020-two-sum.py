class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        s={}
        for i, j in enumerate(nums):
            if target-j in s:
                return [i, s[target-j]]
            s[j]=i

