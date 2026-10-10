class Solution:
    def pattern18(self, n):
        for i in range(0,n):
            for j in range(64+n-i,64+n+1):
                print(chr(j),end=" ")
            print()