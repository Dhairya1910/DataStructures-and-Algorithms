# import numpy as np
# s = "PAYPALISHIRING"
# n = 3 
# dp = np.zeros((0,n))
# max_col = len(s)//n


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        idx, d = 0, 1
        rows = [[] for _ in range(numRows)]

        for char in s:
            rows[idx].append(char)
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d

        for i in range(numRows):
            rows[i] = ''.join(rows[i])
        print(rows)
        return ''.join(rows)   
    


a = Solution()
ans = a.convert("PAYPALISHIRING",4)
print(ans)
