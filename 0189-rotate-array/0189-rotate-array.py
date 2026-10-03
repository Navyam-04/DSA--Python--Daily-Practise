class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse_sub_array(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        n = len(nums)

        if n <= 1:
            return

        k = k % n

        if k == 0:
            return

        # Step 1: Reverse the entire array
        reverse_sub_array(nums, 0, n - 1)

        # Step 2: Reverse the first k elements
        reverse_sub_array(nums, 0, k - 1)

        # Step 3: Reverse the remaining elements
        reverse_sub_array(nums, k, n - 1)
        return nums
    

        