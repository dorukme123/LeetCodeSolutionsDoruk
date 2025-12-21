class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        targetReached = lambda hours, target: 1 if hours >= target else 0
        return sum([targetReached(hour, target) for hour in hours])