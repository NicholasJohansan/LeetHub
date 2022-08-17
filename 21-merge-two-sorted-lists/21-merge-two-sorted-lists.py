# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:        
        list1_pointer = list1
        list2_pointer = list2
        self.tail_pointer = None
        self.head = None
        
                
        def add_to_head(next_val):
            if self.head == None:
                self.head = ListNode(val=next_val)
                self.tail_pointer = self.head
            else:
                self.tail_pointer.next = ListNode(val=next_val)
                self.tail_pointer = self.tail_pointer.next
        
        while list1_pointer or list2_pointer:
            if list1_pointer and list2_pointer:
                if list1_pointer.val <= list2_pointer.val:
                    add_to_head(list1_pointer.val)
                    list1_pointer = list1_pointer.next
                else:
                    add_to_head(list2_pointer.val)
                    list2_pointer = list2_pointer.next
            elif list1_pointer:
                add_to_head(list1_pointer.val)
                list1_pointer = list1_pointer.next
            elif list2_pointer:
                add_to_head(list2_pointer.val)
                list2_pointer = list2_pointer.next
        return self.head
        