class Solution:
    def isPalindrome(self, x: int) -> bool:
        if len(x) == 3:
            return x
        # we need to find the lenght of x
        # need to check if first and last number are the same
        # 0 and -1 if in a list
        # 1 and -2 
        # etc. 
        # or can we reverse the number and == to x?
        # and return true or false?