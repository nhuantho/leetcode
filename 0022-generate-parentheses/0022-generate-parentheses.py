class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenthesis_gen = []

        def backtracking(parenthesis_unit: str, l, r):
            if len(parenthesis_unit) == n * 2:
                parenthesis_gen.append(parenthesis_unit)
                return
            if l < n:
                backtracking(parenthesis_unit + '(', l + 1, r)
            if r < l:
                backtracking(parenthesis_unit + ')', l, r + 1)

        backtracking('', 0, 0)
        return parenthesis_gen