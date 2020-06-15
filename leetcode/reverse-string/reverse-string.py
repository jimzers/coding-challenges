class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        lt = 0
        rt = len(s) - 1 # get right most idx

        while (lt < rt):
            tmp = s[lt]
            s[lt] = s[rt]
            s[rt] = tmp
            # increment pointers
            lt += 1
            rt -= 1
