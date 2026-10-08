class Solution:
    def maxArea(self, height: list[int]) -> int:
        left=0
        right=len(height)-1
        max_water=0
        while left < right:
            cur_height=min(height[left],height[right])
            cur_width=(right-left)
            cur_area=cur_height * cur_width
            if cur_area > max_water:
                max_water=cur_area
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return max_water
        
        