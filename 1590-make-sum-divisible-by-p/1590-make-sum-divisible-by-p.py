class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        target = sum(nums) % p

        if target == 0:
            return 0

        min_length = len(nums)
        current_sum = 0
        rem_map = {0: -1}

        for i in range(len(nums)):
            current_sum = (current_sum + nums[i]) % p

            needed = (current_sum - target) % p

            if needed in rem_map:
                length = i - rem_map[needed]
                min_length = min(min_length, length)

            rem_map[current_sum] = i

        return min_length if min_length < len(nums) else -1
        