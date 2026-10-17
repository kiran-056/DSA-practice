#this is reverse half pyramid containg values of j.
class Solution:
    def pattern6(self, n):
        for i in range(n,0,-1):
            for j in range(1,i+1):
                print(j,end="")
            print()