class Solution:
    def gcd(self, a, b):
        return a if b==0 else gcd(b, a%b)
    def findGCD(self, nums: List[int]) -> int:
        s=nums[0]
        l=nums[0]
        for i in nums:
            if i<s:
                s=i
            if i>l:
                l=i
        return self.gcd(s, l)
        