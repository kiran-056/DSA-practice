class Solution:
    def pattern17(self, n):
       for i in range(1,n+1):
        for j in range(1,n+1-i):
            print(" ",end="")
        s=65
        breakpoint=((2*i-1)/2)
        for k in range(1,2*i):
            print(chr(s),end="")
            if(k<=breakpoint):
                s=s+1
            else:
                s=s-1
        print()