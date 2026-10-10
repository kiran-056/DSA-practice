class Solution:
    def pattern5(self, n):
        for i in range(n,0,-1):
            for j in range(0,i):
                print("*",end="")
            print()