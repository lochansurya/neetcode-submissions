class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter

        freq = Counter(nums)
        heap = [(-count, num) for num, count in freq.items()]
        heapq.heapify(heap)

        arr = lambda heap: (heapq.heappop(heap)[1] for _ in range(len(heap)))
        item = lambda k: (heapq.heappop(heap)[1] for _ in range(k))

        return list(item(k))