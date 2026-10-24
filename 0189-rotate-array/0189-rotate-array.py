class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)
        ind=len(nums)-k
        nums[:]=nums[-k:]+nums[:-k]
        print(nums)