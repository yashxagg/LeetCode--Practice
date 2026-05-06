class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # 1. Compute the length and find the tail
        last_node = head
        length = 1
        while last_node.next:
            last_node = last_node.next
            length += 1
            
        # 2. Adjust k
        k = k % length
        if k == 0:
            return head
            
        # 3. Connect tail to head to make it circular
        last_node.next = head
        
        # 4. Find the new tail: (length - k - 1) steps from head
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
            
        # 5. The new head is the node after the new tail
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head