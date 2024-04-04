import unittest
from solution import ListNode, Solution

class TestReverseLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def create_linked_list(self, vals):
        if not vals:
            return None
        head = ListNode(vals[0])
        current = head
        for val in vals[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def list_to_values(self, head):
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values

    def test_iterative(self):
        head = self.create_linked_list([1, 2, 3, 4, 5])
        reversed_head = self.solution.reverseList_iterative(head)
        self.assertEqual(self.list_to_values(reversed_head), [5, 4, 3, 2, 1])

    def test_recursive(self):
        head = self.create_linked_list([1, 2, 3, 4, 5])
        reversed_head = self.solution.reverseList_recursive(head)
        self.assertEqual(self.list_to_values(reversed_head), [5, 4, 3, 2, 1])

    def test_empty_list(self):
        head = self.create_linked_list([])
        reversed_head = self.solution.reverseList_iterative(head)
        self.assertIsNone(reversed_head)

if __name__ == '__main__':
    unittest.main()
