from logging import exception


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # check for two words or more
      
        if len(str) >=2:
            pass
        else:
            raise exception("Please enter a list of words")
        # check for first letter and second letter match
        # 