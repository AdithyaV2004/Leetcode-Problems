class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda i : i[0])
        l=[intervals[0]]
        for s,e in intervals[1:]:
            end = l[-1][1]
            if s <= end :
                if e>end:
                    l[-1][1] = e
            else:
                l.append([s, e])
        return l
