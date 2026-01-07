class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = [start + 2 * i for i in range(n)]
        xor = arr[0]
        for j in range(len(arr) - 1):
            xor ^= arr[j + 1]
        return xor