class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max=0
        left=0
        right=len(heights)-1
        while left<right:
            w=right-left
            h=min(heights[left],heights[right])
            water=w*h
            if water>max:
                max=water
            if heights[left]<heights[right]:
                left+=1
            elif heights[left]>heights[right]:
                right-=1
            else:
                left+=1
                right-=1
        return max

            
                

        