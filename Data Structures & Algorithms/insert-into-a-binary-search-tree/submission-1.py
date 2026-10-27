# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newNode = TreeNode(val)
        if not root: return newNode
        cur = root
        while cur:
            if cur.val < val:
                if not cur.right: 
                    cur.right = newNode
                    break
                cur = cur.right
            else:
                if not cur.left:
                    cur.left = newNode
                    break
                cur = cur.left

        return root