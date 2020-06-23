class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        uhhh keep a pointer for earliest zero (that hasn't been dealt with)
        that way we can go thru piles of zeros before moving a real element

        keep two pointers: earliest zero

        how to deal with earliest zero: swap the earliestmost nonzero afterwards with the earliest zero
        """
        earliest_zero = None
        num_zeros = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                if num_zeros > 0:
                    nums[earliest_zero] = nums[i]
                    nums[i] = 0
                    earliest_zero += 1
            else:
                if not num_zeros:
                    earliest_zero = i
                num_zeros += 1

        return nums
