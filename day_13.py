class Solution:
    def romanToInt(self, s: str) -> int:
        row = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        res = 0
        i = 0
        for i ,j in zip(s,s[1:]):
            if row[i] < row[j]:
                res -= row[i]
            else:
                res += row[i]

        return res + row[s[-1]]



        