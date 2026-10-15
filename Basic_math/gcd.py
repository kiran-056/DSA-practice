class Solution:
    def GCD(self, n1, n2):
        cf=list()
        for i in range(1,max(n1,n2)+1):
            if(n1%i==0 and n2%i==0):
                cf.append(i)
        g=max(cf)
        return g