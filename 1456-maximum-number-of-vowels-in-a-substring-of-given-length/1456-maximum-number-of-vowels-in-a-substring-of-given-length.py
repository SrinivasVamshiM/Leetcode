class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_vowels = 0
        current_vowels = 0

        # Initialize the count of vowels in the first substring of length k
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1

        max_vowels = current_vowels

        # Slide the window through the string and update max_vowels
        for i in range(k, len(s)):
            if s[i - k] in vowels:  # Remove the leftmost character from the window
                current_vowels -= 1
            if s[i] in vowels:  # Add the new character to the window
                current_vowels += 1
            max_vowels = max(max_vowels, current_vowels)

        return max_vowels