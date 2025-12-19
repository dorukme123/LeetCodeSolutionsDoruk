class Solution:
    def countDigits(self, num: int) -> int:
        digits = list(map(int, str(num)))
        checkDiv = lambda digit, number: True if number % digit == 0 else False   
        return len([x for x in digits if checkDiv(x,num) == True])