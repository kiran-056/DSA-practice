class Solution:
    def countDigit(self, n):
        c=0
        if n==0:
            return 1
        while(n>0):
            lastdigit=n%10
            c=c+1
            n=n//10
        return c