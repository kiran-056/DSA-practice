#this is the code for the square with stars.
class Solution:
    def pattern1(self, n):
        for i in range(0,n):
            for j in range(0,n):
                print("*",end="")
            print()
        