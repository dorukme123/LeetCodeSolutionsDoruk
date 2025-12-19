import re
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([len(re.findall(" ", sentence)) + 1 for sentence in sentences])
