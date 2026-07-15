class Solution:
    def gcd(self, a: int, b: int)->int:
        
        return gcd(b, a%b)

    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd=n*n
        sumEven=n*(n+1)
        return self.gcd(sumOdd, sumEven)
