class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        lower = s.lower()

        wordlist = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"

        while left <= right:
            if lower[left] not in wordlist:
                left += 1
            elif lower[right] not in wordlist:
                right -= 1
            else:
                if lower[left] != lower[right]:
                    return False
                left += 1
                right -= 1
        return True