class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nz=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i], nums[nz]=nums[nz], nums[i]
                nz+=1

