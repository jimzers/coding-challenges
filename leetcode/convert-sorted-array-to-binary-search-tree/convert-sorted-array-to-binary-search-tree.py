# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        midpt = len(nums) // 2
        lt_node = self.sortedArrayToBST(nums[:midpt])
        rt_node = self.sortedArrayToBST(nums[midpt+1:])
        curr_node = TreeNode(nums[midpt], lt_node, rt_node)
        return curr_node
