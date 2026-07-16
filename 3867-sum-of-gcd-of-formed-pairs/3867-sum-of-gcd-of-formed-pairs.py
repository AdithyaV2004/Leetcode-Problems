class Solution:
    def gcd(self, a, b):
        return a if b==0 else gcd(b, a%b)
    def gcdSum(self, nums: list[int]) -> int:
        sum=0
        prefix=[]
        prefixgcd=[]
        l=len(nums)
        g=nums[0]
        prefix.append(g)
        for i in range(1, l):
            g=max(g, nums[i])
            prefix.append(g)
        for i in range(l):
            prefixgcd.append(self.gcd(nums[i], prefix[i]))
        prefixgcd=sorted(prefixgcd)
        lp=0
        rp=l-1
        while lp<rp:
            sum+=self.gcd(prefixgcd[lp], prefixgcd[rp])
            print(sum)
            lp+=1
            rp-=1
        return sum

