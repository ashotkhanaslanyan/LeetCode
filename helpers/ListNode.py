from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(items: List[int]) -> Optional[ListNode]:
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head


def linked_list_to_list(node: Optional[ListNode]) -> List[int]:
    if not node:
        return []
    items = []
    current = node
    while current:
        items.append(current.val)
        current = current.next
    return items