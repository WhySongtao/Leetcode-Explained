# We need two pointers to reach the intersaction at the same time but the length
# of two linked list may differ. So we can fast forward the pointer in the linked
# list with larger length to match the length of the other linked list. To do
# that, we need to know


def getIntersectionNode(headA, headB):
    if (headA is None) or (headB is None):
        return None
    # First, get the length
    A = headA # We don't want to mess up the head pointer.
    count_A = 0
    while A:
        count_A += 1
        A = A.next

    B = headB
    count_B = 0
    while B:
        count_B += 1
        B = B.next

    # Compare the length of linked list A and B. Fast forward one of them.
    if count_A > count_B:
        for _ in range(count_A-count_B):
            headA = headA.next
    elif count_A < count_B:
        for _ in range(count_B-count_A):
            headB = headB.next

    # Now both heads are at the same length. Traverse both list until we found
    # the same node.
    while headA != headB:
        headA = headA.next
        headB = headB.next

    return headA # return any of the head.
