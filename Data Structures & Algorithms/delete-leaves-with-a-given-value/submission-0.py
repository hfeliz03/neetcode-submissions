# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode | None, target: int) -> TreeNode | None:

        parents = deque([])
        needToFindLeaves = 0
        def getLeaves(curNode, parent):
            nonlocal parents
            if not curNode: return
            if not curNode.left and not curNode.right:
                parents.append(parent)
            getLeaves(curNode.left, curNode)
            getLeaves(curNode.right, curNode)
        
        def remover():
            nonlocal parents

            if not root.left and not root.right:
                if root.val == target: return None
                else: return root

            getLeaves(root, None)
            needToFindLeaves = 0

            while parents:
                curParent = parents.popleft()
                #If parent has a child, that child equals target, and that child is a leaf, remove it
                if curParent.left and curParent.left.val == target and not curParent.left.left and not curParent.left.right:
                    curParent.left = None
                if curParent.right and curParent.right.val == target and not curParent.right.left and not curParent.right.right:
                    curParent.right = None
                #If now the parent becomes a leaf you have to redo the process
                if not curParent.left and not curParent.right:
                    needToFindLeaves = 1

            if needToFindLeaves: return remover()
            else: return root
        
        return remover() 