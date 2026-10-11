class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window_sum=sum(nums[:k])
        max_sum=window_sum
        for right in range(k,len(nums)):
            left=right-k
            window_sum=window_sum+nums[right]-nums[left]
            max_sum=max(window_sum,max_sum)
        return max_sum/k
        