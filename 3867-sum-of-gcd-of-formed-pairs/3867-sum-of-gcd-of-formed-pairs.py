class Solution:
    def gcd(self, a, b):
        return a if b==0 else gcd(b, a%b)
    def gcdSum(self, nums: list[int]) -> int:
        sum=0
        l=len(nums)
        g=nums[0]
        for i in range(l):
            g=max(g, nums[i])
            nums[i]=self.gcd(nums[i], g)
        nums.sort()
        lp=0
        rp=l-1
        while lp<rp:
            sum+=self.gcd(nums[lp], nums[rp])
            print(sum)
            lp+=1
            rp-=1
        return sum

