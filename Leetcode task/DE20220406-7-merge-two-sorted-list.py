# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # Solution 1: Use the native ListNode object
        head = mergedLists = ListNode()

        while list1 and list2:
            if list1.val > list2.val:
                mergedLists.next = list2
                list2 = list2.next
            else:
                mergedLists.next = list1
                list1 = list1.next

            mergedLists = mergedLists.next

        if list1:
            mergedLists.next = list1

        if list2:
            mergedLists.next = list2

        return head.next

        # Solution 2: Use the list sorting function and generate ListNode with corresponding element value and next ref
        # tmp = []
        #
        # while list1:
        #     tmp.append(list1.val)
        #     list1 = list1.next
        #
        # while list2:
        #     tmp.append(list2.val)
        #     list2 = list2.next
        #
        # tmp.sort()
        #
        # result = None
        # for i in tmp[::-1]:
        #     result = ListNode(val=i, next=result)
        #
        # return result
