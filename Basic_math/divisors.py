class Solution:
    def divisors(self, n):
        li=list()
        for i in range(1,n+1):
            if(n%i==0):
                li.append(i)
        return li