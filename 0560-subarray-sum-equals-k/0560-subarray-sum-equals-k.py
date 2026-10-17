class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map={0:1}
        current_sum=0
        total_subarrays=0
        for num in nums:
            current_sum=current_sum+num
            needed_sum=current_sum-k
            if needed_sum in prefix_map:
                total_subarrays+=prefix_map[needed_sum]
            prefix_map[current_sum]=prefix_map.get(current_sum,0)+1
        return total_subarrays
       

        