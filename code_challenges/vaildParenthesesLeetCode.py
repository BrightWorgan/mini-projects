class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] == '(' and s[-1] == ')':
            return "Vaild"
        elif s[0] == '{' and s[-1] == '}':
            return "Vaild"
        elif s[0] == '[' and s[-1] == ']':
            return "Vaild"
        else:
            return "Invaild String"