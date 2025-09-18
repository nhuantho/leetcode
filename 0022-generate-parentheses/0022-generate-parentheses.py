class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenthesis_gen = []

        def dfs(parenthesis_unit: List[str]):
            if len(parenthesis_unit) == n * 2:
                parenthesis_gen.append(parenthesis_unit[:])
                return

            parenthesis_unit.append("(")
            dfs(parenthesis_unit)
            parenthesis_unit.pop()

            parenthesis_unit.append(")")
            dfs(parenthesis_unit)
            parenthesis_unit.pop()

        def check_pair_parenthesis(parenthesis_unit: List[str]):
            checkpoint = []
            while parenthesis_unit:
                tmp_p = parenthesis_unit.pop()
                if tmp_p == "(" and len(checkpoint) == 0:
                    return False
                elif tmp_p == "(":
                    tmp_c = checkpoint.pop()
                    if tmp_c == "(":
                        return False
                    else:
                        if len(checkpoint) == 0 and len(parenthesis_unit) == 0:
                            return True
                else:
                    checkpoint.append(tmp_p)
            return False

        dfs([])
        print(parenthesis_gen)

        res = []

        for item in parenthesis_gen:
            tmp = item[:]
            if check_pair_parenthesis(tmp):
                res.append("".join(item[:]))
        return res