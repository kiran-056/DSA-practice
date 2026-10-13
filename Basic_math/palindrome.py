class Solution:
    def isPalindrome(self, n):
        original=n
        rev=0
        while(n>0):
            lastdigit=n%10
            rev=rev*10+lastdigit
            n=n//10
        if(rev==original):
            return True
        else:
            return False