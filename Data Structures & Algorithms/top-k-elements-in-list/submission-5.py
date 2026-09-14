class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1

        buckets = [[] for i in range(len(nums)+1)]

        for key, value in hashmap.items():
            buckets[value].append(key)

        result = []
        for i in range(len(buckets)-1,0,-1):
            if buckets[i] != []:
                result += buckets[i]
            if len(result) == k:
                return result