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
                
                # if alexander contains "IV""IX""XL""XC""CD""CM"
                if re.sub("IV", "4", alexander):
                    return int(alexander)
                if re.sub("IX", "9", alexander):
                    return int(alexander)
                if re.sub("XL", "40", alexander):
                    return int(alexander)
                if re.sub("XC", "90", alexander):
                    return int(alexander)
                if re.sub("CD", "400", alexander):
                    return int(alexander)
                if re.sub("CM", "900", alexander):
                    return int(alexander)
        return alexander
        
    romanToInt("III")