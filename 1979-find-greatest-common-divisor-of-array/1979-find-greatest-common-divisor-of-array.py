class Solution:
    def gcd(self, a, b):
        return a if b==0 else gcd(b, a%b)
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        return self.gcd(nums[0], nums[-1])