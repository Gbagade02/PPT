## 1st Quetion ans
def mySqrt(x):
    left = 0
    right = x

    while left <= right:
        mid = (left + right) // 2
        if mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1

    return right

## 2nd Question Ans
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy_head = ListNode()  # Dummy node for the result linked list
    current = dummy_head  # Pointer to the current node in the result linked list
    carry = 0  # Carry initially 0

    while l1 or l2 or carry:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        sum = x + y + carry
        carry = sum // 10
        current.next = ListNode(sum % 10)
        current = current.next

        # Move to the next nodes if they exist
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy_head.next
