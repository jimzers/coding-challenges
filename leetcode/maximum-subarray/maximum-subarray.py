class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Two options: you either take the element, or you don't take the element.
        If you take the element see if the end result is bigger than just starting fresh.
        If starting fresh is better, you can just take a new array
        """
        max_subarray_sum = float('-inf')
        local_sum = float('-inf')

        for num in nums:
            local_sum = max(local_sum + num, num)
            max_subarray_sum = max(max_subarray_sum, local_sum)

        return max_subarray_sum
