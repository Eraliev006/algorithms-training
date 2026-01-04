
"""

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]


Example 2:
Input: nums = [1], k = 1
Output: [1]
"""

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    """
    SOLVE WITH BUCKETS
    TIME O(N)
    """
    from collections import Counter

    count = Counter(nums)

    buckets = [[] for _ in range(len(nums) + 1)]

    for num, freq in count.items():
        buckets[freq].append(num)

    res = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            res.append(num)
            if len(res) == k:
                return res



def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
    """
    SOLVE WITH SORTING 
    TIME O(N LOG N)
    """
    from collections import Counter

    res = Counter(nums)

    s = sorted(res.keys(), key=lambda x: res[x], reverse=True)[:k]
    return s