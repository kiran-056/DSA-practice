class Solution:
    def pattern14(self, n):
        for i in range(0,n):
            for j in range(0,i+1):
                print(chr(65+j),end="")
            print()