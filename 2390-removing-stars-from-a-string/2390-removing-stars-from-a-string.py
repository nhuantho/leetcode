class Solution:
    def removeStars(self, s: str) -> str:
        non_stars = []
        for i in s:
            if i == "*":
                non_stars.pop()
            else:
                non_stars.append(i)
        return "".join(non_stars)
        