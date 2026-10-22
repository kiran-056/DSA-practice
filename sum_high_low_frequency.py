class Solution:
    def sumHighestAndLowestFrequency(self, nums):
        hash=[0]*100000
        for i in nums:
            hash[i]=hash[i]+1
        unique=list(set(hash))
        unique=sorted(unique)
        min=unique[1]
        max=unique[-1]
        return max+min