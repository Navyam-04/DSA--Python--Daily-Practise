class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        closest_sum=float('inf')
        for i in range(n-2):
            left=i+1
            right=n-1
            while left < right:
                cure_sum=nums[i]+nums[left]+nums[right]
                if abs(target - cure_sum) < abs(target - closest_sum):
                    closest_sum = cure_sum
                if cure_sum==target:
                    return cure_sum
                elif cure_sum > target:
                    right-=1
                else:
                    left+=1
        return closest_sum
        