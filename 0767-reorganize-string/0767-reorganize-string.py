class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap=[[cnt, chr] for chr, cnt in count.items()]
        heapq.heapify_max(maxHeap)
        prev=None
        res=""
        while maxHeap or prev:
            if not maxHeap:
                return ""
            cnt, chr=heapq.heappop_max(maxHeap)
            res+=chr
            cnt-=1
            if prev:
                heapq.heappush_max(maxHeap, prev)
                prev=None
            if cnt>0:
                prev=[cnt, chr]
        return res
