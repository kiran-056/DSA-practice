class Solution:
    def pattern10(self, n):
        for i in range(0,n):
            for j in range(0,i+1):
                print("*",end="")
            print()
        for k in range(n-1,0,-1):
            for j in range(k,0,-1):
                print("*",end="")
            print()
        