class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        finlist = []
        list1 = [1]
        list2 = [1,1]
        finlist.append(list1)
        if numRows == 1:
            return finlist
        finlist.append(list2)
        if numRows == 2:
            return finlist
        for i in range(2, numRows):
            prev = finlist[i-1]
            newrow = [1]
            
            for j in range(1,i):
                newrow.append(prev[j-1]+prev[j])
            newrow.append(1)
            finlist.append(newrow)
        return finlist
            