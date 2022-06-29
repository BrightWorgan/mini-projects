class Solution:
    def romanToInt(self, s: str) -> int:
        import re
        alexander = 0
        # if alexander contains "IV""IX""XL""XC""CD""CM"
        if re.sub("IV", "4", alexander):
            totalCount = re.findall("IV", s).count()
            s = re.sub("IV", "", s)
            alexander += totalCount * 4 
        if re.sub("IX", "9", alexander):
            totalCount = re.findall("IX", s).count()
            s = re.sub("IX", "", s)
            alexander += totalCount * 9
        if re.sub("XL", "40", alexander):
            totalCount = re.findall("XL", s).count()
            s = re.sub("XL", "", s)
            alexander += totalCount * 40
        if re.sub("XC", "90", alexander):
            totalCount = re.findall("XC", s).count()
            s = re.sub("XC", "", s)
            alexander += totalCount * 90
        if re.sub("CD", "400", alexander):
            totalCount = re.findall("CD", s).count()
            s = re.sub("CD", "", s)
            alexander += totalCount * 400
        if re.sub("CM", "900", alexander):
            totalCount = re.findall("XL", s).count()
            s = re.sub("CM", "", s)
            alexander += totalCount * 900


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

        return alexander
        
    romanToInt("III")