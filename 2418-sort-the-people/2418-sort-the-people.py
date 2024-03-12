class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        list1=[]
        d={}
        for i in range(n):
            d[heights[i]] = d.get(heights[i],names[i])
        heights.sort(reverse=True)
        for i in range(n):
            list1.append(d.get(heights[i]))
        return list1