# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sortedList = ListNode(-1)
        sHead = sortedList
        head1 = list1
        head2 = list2

        while (head1 is not None) and (head2 is not None):
            if head1.val < head2.val:
                sHead.next = head1
                head1 = head1.next
            else:
                sHead.next = head2
                head2 = head2.next
            
            sHead = sHead.next
        
        if head1 is not None:
            sHead.next = head1
        else:
            sHead.next = head2

        return sortedList.next
