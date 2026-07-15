class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=r=0
        h={}
        for i in range(len(nums)):
            if nums[i] in h:
                j=h[nums[i]]
                if abs(i-j)<=k:
                    print(i, j)
                    return True                        
            h[nums[i]]=i
        return False