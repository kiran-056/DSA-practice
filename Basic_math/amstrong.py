class Solution:
    def isArmstrong(self, n):
        sum=0
        original=n
        while(n>0):
            lastdigit=n%10
            sum=sum+(lastdigit**3)
            n=n//10
        if(sum==original):
            return True
        else:
            return False