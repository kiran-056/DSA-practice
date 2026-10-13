class Solution:
    def reverseNumber(self, n):
        rev=0
        while(n>0):
            lastdigit=n%10
            rev=rev*10+lastdigit
            n=n//10
        return rev