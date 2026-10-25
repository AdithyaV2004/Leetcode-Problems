class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        def rev(i, j):
            while i<j:
                nums[i], nums[j]=nums[j], nums[i]
                i, j=i+1, j-1
        if k==0:
            return
        n=len(nums)
        k%=n
        rev(0, n-1)
        rev(0, k-1)
        rev(k, n-1)