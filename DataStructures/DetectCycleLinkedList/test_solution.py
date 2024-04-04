import unittest
from solution import ListNode, Solution

class TestLinkedListCycle(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def create_linked_list(self, values, pos):
        if not values:
            return None
        
        head = ListNode(values[0])
        current = head
        
        cycle_start = None
        for i in range(0, len(values)):
            current.next = ListNode(values[i])
            current = current.next
            if i == pos:
                cycle_start = current
        
        if pos != -1:
            current.next = cycle_start
        
        return head

    def test_has_cycle(self):
        head = self.create_linked_list([3, 2, 0, -4], 1)
        self.assertTrue(self.solution.hasCycle(head))

        head = self.create_linked_list([1, 2], 0)
        self.assertTrue(self.solution.hasCycle(head))

    def test_no_cycle(self):
        head = self.create_linked_list([1], -1)
        self.assertFalse(self.solution.hasCycle(head))

        head = self.create_linked_list([], -1)
        self.assertFalse(self.solution.hasCycle(head))

if __name__ == '__main__':
    unittest.main()
