# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_reversed_number(self, l: ListNode):
        number = 0
        node = l
        multiplier = 1
        while node:
            number = number + node.val * multiplier
            multiplier *= 10
            node = node.next
        return number

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = self.get_reversed_number(l1)
        n2 = self.get_reversed_number(l2)
        num = str(n1 + n2)
        head = None
        for i in range(len(num)):
            node = ListNode(val=int(num[i]), next=head)
            head = node
        return head
            
        