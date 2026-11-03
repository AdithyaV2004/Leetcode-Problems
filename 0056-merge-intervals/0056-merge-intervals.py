class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda i : i[0])
        l=[intervals[0]]
        for s,e in intervals[1:]:
            end = l[-1][1]
            if s <= end :
                l[-1][1]=max(e, end)
            else:
                l.append([s, e])
        return l
