# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        rightNode = head
        tempLeft = None
        index = 1

        while rightNode and index <= right:
            if index == left - 1:
                tempLeft = rightNode

            rightNode = rightNode.next
            index += 1

        tempRight = rightNode

        # start of section to reverse
        cur = tempLeft.next if tempLeft else head

        # original left node becomes the tail after reversal
        reverseTail = cur

        prev = tempRight
        count = right - left + 1

        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1

        # reconnect left side
        if tempLeft:
            tempLeft.next = prev
            return head
        else:
            return prev
