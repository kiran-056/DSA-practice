class Solution:
    def selectionSort(self, nums):
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        return nums