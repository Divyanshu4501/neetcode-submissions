class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0

        while l < r:
            h_l, h_r = height[l], height[r]
            if h_l < h_r:
                a = h_l * (r - l)
                l += 1
            else:
                a = h_r * (r - l)
                r -= 1

            if a > area:
                area = a

        return area