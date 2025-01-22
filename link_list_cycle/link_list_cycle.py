class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        dummy = ListNode(None)
        dummy.next = head
        slow = fast = dummy

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow is fast:
                return True
        return False

# Helper function to create a linked list from a list and optionally create a cycle
def createLinkedList(values, pos):
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    cycle_node = None

    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        if i == pos:
            cycle_node = current

    if pos != -1:
        current.next = cycle_node

    return head

# Example usage
solution = Solution()

# Create a linked list [3, 2, 0, -4] with a cycle at position 1
head = createLinkedList([3, 2, 0, -4], 1)
print(solution.hasCycle(head))  # Output: True

# Create a linked list [1, 2] with a cycle at position 0
head = createLinkedList([1, 2], 0)
print(solution.hasCycle(head))  # Output: True

# Create a linked list [1] with no cycle
head = createLinkedList([1], -1)
print(solution.hasCycle(head))  # Output: False
