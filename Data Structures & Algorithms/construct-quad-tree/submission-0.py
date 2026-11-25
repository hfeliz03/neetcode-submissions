"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(subgrid): 
            isSameVal = set()
            for row in subgrid:
                for num in row:
                    isSameVal.add(num)
                    if len(isSameVal) > 1: break
                if len(isSameVal) > 1: break

            if len(isSameVal) == 1:
                return Node(isSameVal.pop(), 1, None, None, None, None)

            else:
                m, n = len(subgrid)//2, len(subgrid[0])//2
                a = [row[:n] for row in subgrid[:m]]
                b = [row[n:] for row in subgrid[:m]]
                c = [row[:n] for row in subgrid[m:]]
                d = [row[n:] for row in subgrid[m:]]

                return Node(0, 0, 
                    helper(a), 
                    helper(b), 
                    helper(c), 
                    helper(d))

        Qtree = Node(-1, 0, helper(grid), None, None, None)
        return Qtree.topLeft