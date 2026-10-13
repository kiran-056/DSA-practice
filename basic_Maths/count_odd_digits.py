class Solution:
    def countOddDigit(self, n):
        c=0
        while(n>0):
            lastdigit=n%10
            if(lastdigit%2!=0):
                c=c+1
            n=n//10
        return c