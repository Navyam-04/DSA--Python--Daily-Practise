class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        n=len(nums)
        nums.sort()
        count=0
        for i in range(n-1,1,-1):
            c=nums[i]
            left=0
            right=i-1
            while left < right:
                if nums[left]+nums[right] >c:
                    count+=(right-left)
                    right-=1
                else:
                    left+=1
        return count
        