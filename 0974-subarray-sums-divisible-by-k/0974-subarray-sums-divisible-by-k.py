class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        prefix_map={0:1}
        current_sum=0
        subarrays=0
        for num in nums:
            current_sum+=num
            remainder=((current_sum % k)+k)% k
            if remainder in prefix_map:
                subarrays+=prefix_map[remainder]
            prefix_map[remainder]=prefix_map.get(remainder,0)+1
        return subarrays

        