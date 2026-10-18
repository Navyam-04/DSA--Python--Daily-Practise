class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        n=len(nums)
        lesser=[]
        greater=[]
        equal=[]
        for i in range(len(nums)):
            if nums[i]< pivot:
                lesser.append(nums[i])
            elif nums[i] > pivot:
                greater.append(nums[i])
            else:
                equal.append(nums[i])
        return  lesser + equal + greater
            
        