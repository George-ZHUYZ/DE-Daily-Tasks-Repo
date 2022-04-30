# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        tmpList = []
        for l in lists:
            while l:
                tmpList.append(l.val)
                l = l.next

        tmpList.sort()

        #         result = None
        #         for i in tmpList[::-1]:
        #             result = ListNode(val=i, next=result)

        #         return result

        head = ListNode(0)
        mergedList = head
        for i in tmpList:
            mergedList.next = ListNode(i)
            mergedList = mergedList.next

        return head.next
