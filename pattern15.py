class Solution:
    def pattern15(self, n):
        for i in range(n,0,-1):
            for j in range(0,i):
                print(chr(65+j),end="")
            print()