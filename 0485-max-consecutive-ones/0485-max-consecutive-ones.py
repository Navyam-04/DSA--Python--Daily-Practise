class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        if not nums:
            return 0
        current_count=0
        max_count=0
        for i in nums:
            if i==1:
                current_count+=1
                if current_count > max_count:
                    max_count=current_count
            else:
                current_count=0
        return max_count 
        