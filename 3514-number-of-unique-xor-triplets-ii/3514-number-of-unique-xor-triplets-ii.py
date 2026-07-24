class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        m=max(nums)
        u=2**m.bit_length()
        seen=[False]*u
        n=len(nums)
        for i in range(n):
            for j in range(i, n):
                seen[nums[i]^nums[j]]=True
        third=[False]*u
        for i in range(u):
            if not seen[i]:
                continue
            for v in nums:
                third[i^v]=True
        return sum(True for i in third if i)