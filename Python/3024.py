class Solution:
    def triangleType(self, nums: List[int]) -> str:
        triangle = {
            "a": nums[0] + nums[1],
            "b": nums[0] + nums[2],
            "c": nums[1] + nums[2]
        }
        aSide = triangle.get("a")
        bSide = triangle.get("b")
        cSide = triangle.get("c")
        if aSide == bSide == cSide:
            return "equilateral"
        if aSide > nums[2] and bSide > nums[1] and cSide > nums[0]:
            if aSide != bSide and aSide != cSide and bSide != cSide:
                return "scalene"
            else:
                return "isosceles"
        else:
            return "none"