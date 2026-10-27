class Solution:
    def mergeSort(self, nums):
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        return self.merge(left,right)
    def merge(self,left,right):
        i=0
        j=0
        result=[]
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                result.append(left[i])
                i=i+1
            else:
                result.append(right[j])
                j=j+1
        result.extend(left[i:])
        result.extend(right[j:])
        return result