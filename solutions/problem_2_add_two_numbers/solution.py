from helpers.ListNode import ListNode
from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        current = result
        decimal_point = 0
        while l1 or l2 or decimal_point:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            num_sum = num1 + num2 + decimal_point
            decimal_point = num_sum // 10
            value = num_sum % 10
            current.next = ListNode(value)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            current = current.next
        return result.next
