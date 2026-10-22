class Solution:
    def secondMostFrequentElement(self, nums):
        hash=[0]*100000
        for i in nums:
            hash[i]=hash[i]+1
        unique=list(set(hash))
        unique=sorted(unique)
        s=unique[-2]
        if hash.index(s)==0:
            return -1
        return hash.index(s)