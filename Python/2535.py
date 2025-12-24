import math
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(sum(nums) - sum(list(map(int, "".join([str(num) for num in nums if num != 0])))))