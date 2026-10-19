class Solution:
    def canJump(self, nums: list[int]) -> bool:
        target_index=len(nums)-1
        max_reachable=0
        for i in range(len(nums)):
            if i > max_reachable:
                return False
            max_reachable=max(max_reachable,i+nums[i])
            if max_reachable >= target_index:
                return True
        return True
        