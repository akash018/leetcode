import math


class Solution:
    def reverse(self, x: int) -> int:
        if x >= math.pow(-2, 31) and x <= math.pow(2, 31) - 1:
            strx2 = ''
            if x > 0:
                strx = str(x)
                lenx = len(strx)
                for i in range(lenx):
                    strx2 += strx[-(i+1)]

            else:
                strx = str(x*(-1))
                lenx = len(strx)
                strx2 = ''
                for i in range(lenx):
                    strx2 += strx[-(i+1)]

            if int(strx2) >= math.pow(-2, 31) and int(strx2) <= math.pow(2, 31) - 1:
                if x > 0:
                    return int(strx2)
                else:
                    return int(strx2)*(-1)
            else:
                return 0
        else:
            return 0
