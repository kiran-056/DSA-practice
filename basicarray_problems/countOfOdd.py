class Solution:
    def countOdd(self, arr, n):
        s=0
        for i in range(0,n):
            if arr[i]%2!=0:
                s=s+1
        return s