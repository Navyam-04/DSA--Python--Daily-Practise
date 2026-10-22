import collections
class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        sum_counts=collections.defaultdict(int)
        for a in nums1:
            for b in nums2:
                sum_counts[a+b]+=1
        totals_tuples=0
        for c in nums3:
            for d in nums4:
                target=-(c+d)
                if target in sum_counts:
                    totals_tuples+=sum_counts[target]
        return totals_tuples
        
        