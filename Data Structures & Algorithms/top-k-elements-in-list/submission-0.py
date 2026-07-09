class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num,0) + 1
        sorted_counts = sorted(counts.items(),key = lambda pair:pair[1], reverse = True)
        top_k = sorted_counts[:k]
        result = [pair[0] for pair in top_k]
        return result