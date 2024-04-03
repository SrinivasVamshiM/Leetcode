# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def helper(root, isleft, depth):
            if not root:
                return depth
            if isleft:
                depth = max(depth,helper(root.right,False,depth+1),helper(root.left,True,0))
            else:
                depth = max(depth,helper(root.left,True,depth+1),helper(root.right,False,0))
            return depth
            
        return max(helper(root.left,True, 0), helper(root.right, False, 0))