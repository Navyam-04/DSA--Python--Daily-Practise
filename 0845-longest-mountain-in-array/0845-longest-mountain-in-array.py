class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        max_mount=0
        n=len(arr)
        if n < 3:
            return 0
        for i in range(1,n-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                left=i-1
                while left > 0 and arr[left-1] < arr[left]:
                    left-=1
                right=i+1
                while right < n-1 and arr[right] > arr[right+1]:
                    right+=1
                current_mount=(right-left)+1
                if current_mount > max_mount:
                    max_mount=current_mount
        return max_mount
        