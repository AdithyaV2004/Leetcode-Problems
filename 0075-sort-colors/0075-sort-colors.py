class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n=len(nums)
        i, j, k=0, 0, n-1
        while j<=k:
            if nums[j]==1:
                j+=1
            elif nums[j]==0:
                nums[i], nums[j]=nums[j], nums[i]
                i, j=i+1,j+1
            else:
                nums[k], nums[j]=nums[j], nums[k]
                k-=1
