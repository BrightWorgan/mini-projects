class Solution:
    def romanToInt(self, s: str) -> int:
        import re
        alexander = 0
        for i in s:
            if i == "I":
                alexander += 1
            if i == "V":
                alexander += 5
            if i == "X":
                alexander += 10
            if i == "L":
                alexander += 50
            if i == "C":
                alexander += 100
            if i == "D":
                alexander += 500
            if i == "M":
                alexander += 1000
                # I before V and X
                # X before L and C
                # C before D and M
                # if alexander == "IV""IX""XL""XC""CD""CM"
                if re.match(" +", alexander ):
                    return int(alexander)-1
        return alexander
        
    romanToInt("III")