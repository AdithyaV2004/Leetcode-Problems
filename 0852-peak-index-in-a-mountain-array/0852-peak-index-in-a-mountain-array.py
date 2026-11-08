class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        l, r = 0, len(arr)-1
        while l<r:
            mid=(l+r)//2
            if arr[mid] < arr[mid+1]:
                l = mid + 1
            else:
                r = mid  #mid could be the peak. So dont leave it
        return l