class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        get a hashmap of character counts in s
        go thru t and see if the hashmap count is the same

        this is O(n)
        """

        # lol len check why not
        if len(s) != len(t):
            return False

        letter_map = {}
        num_chars = 0

        for letter in s:
            letter_map[letter] = letter_map.get(letter, 0) + 1
            if letter_map[letter] == 1:  # newly initialized character
                num_chars += 1

        for letter in t:
            letter_map[letter] = letter_map.get(letter, 0) - 1
            if letter_map[letter] == 0:  # all instances of the char has been eliminated
                num_chars -= 1
            if letter_map[letter] < 0: # covers missing character case and overshoot letters
                return False

        return num_chars == 0
