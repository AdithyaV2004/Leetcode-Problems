class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        c=Counter(nums)
        s = sorted(list(c.items()), key = lambda x: x[1], reverse= True)
        return [x[0] for x in s[:k]]
        