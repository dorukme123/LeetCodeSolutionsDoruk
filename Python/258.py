class Solution:
    def addDigits(self, num: int) -> int:
        answer = sum(int(x) for x in list(str(num)))
        return answer if answer < 10 else Solution.addDigits(self, answer)