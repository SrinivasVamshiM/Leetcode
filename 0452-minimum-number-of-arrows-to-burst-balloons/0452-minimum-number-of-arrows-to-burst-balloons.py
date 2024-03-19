class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # Sort the points based on the end coordinate
        points.sort(key=lambda x: x[1])
        print(points)
        arrows = 1
        end = points[0][1]
        print(end)
        for i in range(1, len(points)):
            if points[i][0] > end:
                # If the current balloon's start is beyond the end, we need another arrow
                arrows += 1
                end = points[i][1]
                print(end)
        
        return arrows