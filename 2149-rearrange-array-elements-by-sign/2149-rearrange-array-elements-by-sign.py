class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n=len(nums)
        result=[0]*n
        pos_int=0
        neg_int=1
        for num in nums:
            if num > 0:
                result[pos_int]=num
                pos_int+=2
            else:
                result[neg_int]=num
                neg_int+=2
        return result
        