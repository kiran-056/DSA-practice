class Solution:
    def mostFrequentElement(self, nums):
        hash=[0]*100000
        for i in nums:
            hash[i]=hash[i]+1
        max=0
        for i in hash:
            if max<i:
                max=i
        return hash.index(max)