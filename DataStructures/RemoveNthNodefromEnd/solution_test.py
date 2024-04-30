import unittest
from solution import ListNode, Solution

class TestSolution(unittest.TestCase):
    def create_linked_list(self, values):
        dummy = ListNode()
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    def get_values(self, head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values

    def test_removeNthFromEnd(self):
        solution = Solution()
        
        # Test case 1
        head1 = self.create_linked_list([1, 2, 3, 4, 5])
        expected1 = [1, 2, 3, 5]
        result1 = solution.removeNthFromEnd(head1, 2)
        self.assertEqual(self.get_values(result1), expected1)

        # Test case 2
        head2 = self.create_linked_list([1])
        expected2 = []
        result2 = solution.removeNthFromEnd(head2, 1)
        self.assertEqual(self.get_values(result2), expected2)

        # Test case 3
        head3 = self.create_linked_list([1, 2])
        expected3 = [1]
        result3 = solution.removeNthFromEnd(head3, 1)
        self.assertEqual(self.get_values(result3), expected3)

if __name__ == '__main__':
    unittest.main()
