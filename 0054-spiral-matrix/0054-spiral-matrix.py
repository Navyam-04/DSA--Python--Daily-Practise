class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        if not matrix:
            return res
    
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # Traverse from left to right along the top row
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1
            
            # Traverse from top to bottom along the right column
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1
            
            # Traverse from right to left along the bottom row (if still valid)
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1
                
            # Traverse from bottom to top along the left column (if still valid)
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1
                
        return res