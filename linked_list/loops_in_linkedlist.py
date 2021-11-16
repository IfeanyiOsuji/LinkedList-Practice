class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)

    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)
        return

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(int(str(node.value)))
            node = node.next
        return out






list_with_loop = LinkedList([2, -1, 3, 0, 5])
# creating a loop where the last node points to the second node
loop_start = list_with_loop.head.next
node = list_with_loop.head
while node.next:
    node = node.next
node.next = loop_start


def is_circular(linked_list):
    if linked_list.head == None:
        return False
    slow = linked_list.head
    fast = linked_list.head
    while fast and fast.next:
        # slow pointer moves one node
        slow = slow.next
        # fast pointer moves two node
        fast = fast.next.next
        if slow == fast:
            return True
    # If we get to a node where fast doesn't have a next node or doesn't exist itself,
    # the list has an end and isn't circular
    return False

# Test Cases

# Create another circular linked list
small_loop = LinkedList([0])
small_loop.head.next = small_loop.head

print("Pass" if is_circular(list_with_loop) else "Fail")  # Pass
print("Pass" if is_circular(LinkedList([-4, 7, 2, 5, -1])) else "Fail")  # Fail
print("Pass" if is_circular(LinkedList([1])) else "Fail")  # Fail
print("Pass" if is_circular(small_loop) else "Fail")  # Pass
print("Pass" if is_circular(LinkedList([])) else "Fail")  # Fail

