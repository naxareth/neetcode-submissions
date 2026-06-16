class Solution:
    def isPalindrome(self, s: str) -> bool:
        #1. clean the string — only keep letters and numbers, make everything lowercase
        clean_chars = "".join(char for char in s if char.isalnum()).lower()
        #2. set left pointer at start (index 0)
        left_char = 0
        #3. set right pointer at end (index -1)
        right_char = len(clean_chars) - 1
        #4. while left < right:
        while left_char < right_char:
        #- compare s[left] and s[right]
        #- if they're not equal → not a palindrome, return False
            if clean_chars[left_char] != clean_chars[right_char]:
                return False
        #- if they are equal → move left forward, move right backward
            else:
                left_char += 1
                right_char -= 1

        #5. if loop finishes without returning False → it IS a palindrome, return True
        return True