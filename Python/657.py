class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if moves == "":
            return True
        movesList = list(map(str, moves))
        if movesList.count("U") == movesList.count("D") and movesList.count("L") == movesList.count("R"):
            return True
        else:
            return False
