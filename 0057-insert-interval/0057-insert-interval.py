class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)
        if n == 0:
            intervals.append(newInterval)
            return intervals
        for i in range(n):
            if newInterval[1]<intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0]>intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1],intervals[i][1])]
        res.append(newInterval)
        return res
            