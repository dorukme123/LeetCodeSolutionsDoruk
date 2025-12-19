import string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return True if string.ascii_lowercase == "".join(sorted(list(set(sentence)))) else False