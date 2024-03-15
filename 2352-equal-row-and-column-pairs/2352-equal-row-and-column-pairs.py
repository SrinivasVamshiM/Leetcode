class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rand = 0
        collist = []
        while(rand != n):
            list1 = []
            for i in grid:
                list1.append(i[rand])
            collist.append(list1)
            rand+= 1
        count = 0
        print(grid)
        print(collist)
        for j in range(n):
            for k in range(n):
                if grid[j] == collist[k]:
                    count += 1
        return count