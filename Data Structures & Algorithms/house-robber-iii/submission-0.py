# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def explore(parentBrokenInto, curNode):
            if not curNode: return 0
            if curNode and not curNode.left and not curNode.right: return curNode.val if not parentBrokenInto else 0
            if not parentBrokenInto:
                return max(explore(0, curNode.left) + explore(0, curNode.right),
                        curNode.val + explore(1, curNode.left) + explore(1, curNode.right)
                    )
            else:
                return explore(0, curNode.left) + explore(0, curNode.right)
        

        return max(root.val + explore(1, root.left) + explore(1, root.right), 
                explore(0, root.left) + explore(0, root.right)
                )