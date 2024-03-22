# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(root1, val):
            if not root1:
                return None
            if root1.val == val:
                return root1
            elif root1.val<val:
                return search(root1.right,val)
            else:
                return search(root1.left,val)
    
        return search(root,val)