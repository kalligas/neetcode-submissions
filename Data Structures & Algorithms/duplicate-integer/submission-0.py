from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        return any(count > 1 for count in counts.values())