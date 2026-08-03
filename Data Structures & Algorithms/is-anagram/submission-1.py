from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = Counter(s)
        counts2 = Counter(t)

        for char in counts:
            if char not in counts2:
                return False
            if counts[char] != counts2[char]:
                return False

        return True