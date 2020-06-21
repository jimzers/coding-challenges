class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        keep a hashtable with the counts to each number... can lookup with each call to the table anywayxs.
        should be o(n)

        this is 'easy' soln... o(n) memory as well tho
        """
#         table = {}
#         for num in nums:
#             table[num] = table.get(num, 0) + 1
#             if table[num] > len(nums) / 2:
#                 return num

        """
        Use less memory by keeping a counter of a 'current' number
        Since the result is going to appear more than n/2 than every other number (totaled!)
        we can keep a number of 'majority' elems
        """
        count = 0
        major_num = None
        for num in nums:
            if not count:
                major_num = num
            if num == major_num:
                count += 1
            else:
                count -= 1

        return major_num
