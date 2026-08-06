def digProd(n):
    p=1
    while n>0:
        p*=n%10
        n//=10
    return p
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            if digProd(n)%t==0:
                return n
            n+=1
