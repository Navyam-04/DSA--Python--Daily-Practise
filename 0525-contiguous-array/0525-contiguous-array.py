class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_map={0:-1}
        current_sum=0
        max_length=0
        for i in range(len(nums)):
            if nums[i]==1:
                current_sum+=1
            else:
                current_sum-=1
            if current_sum in prefix_map:
                current_length=i-prefix_map[current_sum]
                max_length=max(max_length,current_length)
            else:
                prefix_map[current_sum]=i
        return max_length
        