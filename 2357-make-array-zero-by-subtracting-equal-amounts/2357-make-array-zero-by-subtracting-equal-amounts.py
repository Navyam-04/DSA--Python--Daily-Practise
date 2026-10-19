class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        uniques=set(nums)
        if 0 in uniques:
            uniques.remove(0)
        return len(uniques)