class Solution:
    def largestDigit(self, n):
        max=0
        while(n>0):
            lastdigit=n%10
            if(lastdigit>max):
                max=lastdigit
            n=n//10
        return max