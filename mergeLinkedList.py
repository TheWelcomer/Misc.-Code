class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1, list2):
    result = None
    resPointer = result
    list1Pointer, list2Pointer = list1.next, list2.next
    while not (list1 == None and list2 == None):
        if list1 == None:
            newNode = ListNode(list2Pointer.val, list2Pointer.next)
            list2Pointer = list2Pointer.next
            resPointer.next = newNode
            resPointer = resPointer.next
        elif list2 == None:
            newNode = ListNode(list1Pointer.val, list1Pointer.next)
            list1Pointer = list1Pointer.next
            resPointer.next = newNode
            resPointer = resPointer.next
        else:
            if list1Pointer.val <= list2Pointer.val:
                newNode = ListNode(list1Pointer.val, list1Pointer.next)
                list1Pointer = list1Pointer.next
                resPointer.next = newNode
                resPointer = resPointer.next
            else:
                newNode = ListNode(list1Pointer.val, list1Pointer.next)
                list1Pointer = list1Pointer.next
                resPointer.next = newNode
                resPointer = resPointer.next
    return result

print()