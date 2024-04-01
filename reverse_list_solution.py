class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


    def insert(self, value=None):
        new_node = Node(i)
        if not self:
            self.next = new_node
        else:
            new_node.next = self.next
            self.next = new_node


class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_beginning(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def reverse_list(self, curr_node: Node) -> Node:
        if not curr_node or not curr_node.next:
            return curr_node
        prev = self.reverse_list(curr_node.next)
        curr_node.next.next = curr_node
        curr_node.next = None
        return prev

    def print(self):
        node = self.head
        while node != None:
            print(node)
            node = node.next


class Solution:

    def reverse_list(self, curr_node: Node) -> Node:
        if not curr_node or not curr_node.next:
            return curr_node
        prev = self.reverse_list(curr_node.next)
        curr_node.next.next = curr_node
        curr_node.next = None
        return prev

    def get_value(self, node: Node):
        return 0 if node is None else node.value

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = Node(0)
        current_node = dummy

        while carry or l1 or l2:
            if l1:
                carry += l1.value
                l1 = l1.next
            if l2:
                carry += l2.value
                l2 = l2.next

            current_node.next = Node(carry % 10)
            carry //= 10
            current_node = current_node.next

        return dummy.next


def fill_list(arr):
    linked_list = None
    for i in arr:
        new_node = Node(i)
        if not linked_list:
            linked_list = new_node
        else:
            new_node.next = linked_list
            linked_list = new_node

    return linked_list


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [1, 2, 3, 4, 5, 6]

    linked_list1 = fill_list(list1)

    linked_list2 = fill_list(list2)

    solution = Solution()
    solution.addTwoNumbers(linked_list1, linked_list2)
