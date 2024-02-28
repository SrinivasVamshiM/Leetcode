class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cl = len(cost)
        total = 0
        mincost=[0]*(cl)
        if cl == 2 :
            return min(cost)
        mincost[0] = cost[0]
        mincost[1] = cost[1]
        
        for i in range(2,cl):
            mincost[i] = min(mincost[i-1],mincost[i-2]) + cost[i]
        
        return min(mincost[cl-1],mincost[cl-2])