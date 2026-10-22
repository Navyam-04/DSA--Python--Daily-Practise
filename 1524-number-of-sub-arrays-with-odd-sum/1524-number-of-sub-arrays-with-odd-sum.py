class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        mod=10**9 +7
        even_count=1
        odd_count=0
        current_sum=0
        total_subarrays=0
        for num in arr:
            current_sum+=num
            if current_sum % 2==0:
                total_subarrays+=odd_count
                even_count+=1
            else:
                total_subarrays+=even_count
                odd_count+=1
        return total_subarrays % mod

        