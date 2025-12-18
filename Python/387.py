from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = defaultdict(int)
        for char in s:
            counts[char] += 1
        result = min(counts, key=counts.get)
        if counts[result] == 1:
            return s.find(result)
        else:
            return -1