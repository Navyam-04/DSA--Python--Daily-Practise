class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        prefix_map={0:1}
        current_sum=0
        subarrays=0
        for num in nums:
            current_sum+=(num%2)
            needed_sum=current_sum-k
            if needed_sum in prefix_map:
                subarrays+=prefix_map[needed_sum]
            prefix_map[current_sum]=prefix_map.get(current_sum,0)+1
        return subarrays
        