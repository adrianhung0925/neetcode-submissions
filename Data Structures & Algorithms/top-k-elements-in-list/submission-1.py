class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1

        buckets = [[] for i in range(len(nums) + 1)]
        for key, value in hashmap.items():
            buckets[value].append(key)

        results = []
        for i in range(len(buckets)-1,0,-1):
            if buckets[i] != []:
                results += buckets[i]
            if len(results) == k:
                return results
        return results