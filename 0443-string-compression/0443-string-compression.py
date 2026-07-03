class Solution:
    def compress(self, chars: List[str]) -> int:
        cnt = 1
        self.index = 1
        l_c = len(chars)

        def handle_num_compress(cnt):
            tmp = []
            while cnt:
                tmp.append(str(cnt % 10))
                cnt //= 10
            tmp = tmp[::-1]
            for i in range(len(tmp)):
                chars[self.index] = tmp[i]
                self.index += 1

        for i in range(1, l_c):
            if chars[i] != chars[i - 1]:
                if cnt > 1:
                    handle_num_compress(cnt)
                chars[self.index] = chars[i]
                self.index += 1
                cnt = 1
            else:
                cnt += 1
        if self.index >= l_c and cnt > 1:
            handle_num_compress(cnt)
        elif cnt > 1:
            handle_num_compress(cnt)
            
        return self.index
