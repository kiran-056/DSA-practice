#this is the code for the half pyramids with i values.
class Solution:
    def pattern4(self, n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(i,end='')
            print()