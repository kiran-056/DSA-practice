class Solution:
    def pattern9(self, n):
        for i in range(0,n):
            for j in range(0,n-i-1):
                print(" ",end="")
            for k in range(0,2*i+1):
                print("*",end="")
            print()
        for m in range(n,0,-1):
            for l in range(n-m,0,-1):
                print(" ",end="")
            for p in range(2*m-1,0,-1):
                print("*",end="")
            print()