class Solution:
    def isPalindrome(self, x: int) -> bool:
        z = str(x)
        for n in range(0, len(z)/2):
            if z[n] == z[-n-1]:
                pass
            else:
                return False
        return True