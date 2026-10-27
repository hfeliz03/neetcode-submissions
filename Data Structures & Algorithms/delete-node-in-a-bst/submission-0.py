class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:

        def leaf(parent, cur):
            if parent.left == cur:
                parent.left = None
            else:
                parent.right = None

        def oneChild(parent, cur):
            child = cur.left if cur.left else cur.right

            if parent.left == cur:
                parent.left = child
            else:
                parent.right = child

        def twoChildren(cur):
            parentSucc = cur
            succ = cur.right

            while succ.left:
                parentSucc = succ
                succ = succ.left

            # Copy successor value
            cur.val = succ.val

            # Delete successor node
            if not succ.left and not succ.right:
                leaf(parentSucc, succ)
            else:
                oneChild(parentSucc, succ)

        # root special case
        dummy = TreeNode(0)
        dummy.left = root

        parent = dummy
        cur = root

        while cur:
            if key < cur.val:
                parent = cur
                cur = cur.left

            elif key > cur.val:
                parent = cur
                cur = cur.right

            else:
                if not cur.left and not cur.right:
                    leaf(parent, cur)

                elif cur.left and cur.right:
                    twoChildren(cur)

                else:
                    oneChild(parent, cur)

                break

        return dummy.left