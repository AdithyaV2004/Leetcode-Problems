class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=len(nums)
        s=set()
        lim=min(l, k+1)
        for i in range(lim):
            if nums[i] in s:
                return True
            s.add(nums[i])
        for i in range(k+1, l):
            s.remove(nums[i-k-1])
            if nums[i] in s:
                return True
            s.add(nums[i])
        return False