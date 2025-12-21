class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        palindromic = lambda curr: True if curr == curr[::-1] else False
        for word in words:
            if palindromic(word) == True:
                return word
            continue
        return ""