class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # naive: use hash table and increment twice
        lookup = set()
        for num in nums:
            if num in lookup:
                lookup.remove(num)
            else:
                lookup.add(num)
        return lookup.pop()
