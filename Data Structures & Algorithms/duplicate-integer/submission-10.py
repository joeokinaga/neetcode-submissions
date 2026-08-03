from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)

        if len(nums) != len(counts):
            return True

        return False