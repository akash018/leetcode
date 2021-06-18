class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        if(strx[::-1]==strx):
            return True
        return False