import copy
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        dCopyNums = copy.deepcopy(nums) 
        afterRounds: list = []
        if not nums:
            return []
        for i in range(len(dCopyNums)): # number of rounds always even
            if not dCopyNums:
                return afterRounds
            alice = min(dCopyNums)
            dCopyNums.remove(alice)
            bob = min(dCopyNums)
            dCopyNums.remove(bob)
            afterRounds.append(bob)
            afterRounds.append(alice)
        return afterRounds