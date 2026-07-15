class Solution:
    def gcd(self, a: int, b: int)->int:
        while b:
            a, b=b, a%b
        return a

    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd=n*n
        sumEven=n*(n+1)
        return self.gcd(sumOdd, sumEven)
