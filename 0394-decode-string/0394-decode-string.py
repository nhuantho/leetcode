class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for c in s:
            if c == "]":
                tmp = ""
                while True:
                    top_v = st.pop()
                    if top_v == "[":
                        break
                    tmp = top_v + tmp
                num = ""
                while True:
                    if len(st) == 0:
                        break
                    tmp_num = st.pop()
                    if tmp_num.isnumeric():
                        num = tmp_num + num
                    else:
                        st.append(tmp_num)
                        break
                tmp = int(num) * tmp
                st.append(tmp)
            else:
                st.append(c)
        return "".join(st)
                

        