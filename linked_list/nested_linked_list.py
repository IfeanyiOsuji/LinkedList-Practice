class Node:
    def __init__(self,
                 value):  # <-- For simple LinkedList, "value" argument will be an int, whereas, for NestedLinkedList, "value" will be a LinkedList
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


# User defined class
class LinkedList:
    def __init__(self, head):  # <-- Expects "head" to be a Node made up of an int or LinkedList
        self.head = head

    '''
    For creating a simple LinkedList, we will pass an integer as the "value" argument
    For creating a nested LinkedList, we will pass a LinkedList as the "value" argument
    '''

    def append(self, value):

        # If LinkedList is empty
        if self.head is None:
            self.head = Node(value)
            return

        # Create a temporary Node object
        node = self.head

        # Iterate till the end of the currrent LinkedList
        while node.next is not None:
            node = node.next

        # Append the newly creataed Node at the end of the currrent LinkedList
        node.next = Node(value)

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(int(str(node.value)))
            node = node.next
        return out


""" Flattening a nested linkedlist"""
class NestedLinkedList(LinkedList):
    """In a nested linkedlist object, each class will be a simple linked list of itself"""
    def flatten(self):
        return self._flatten(self.head)

    def _flatten(self, node):
        if node.next is None:
            return merge(node.value, None)
        return merge(node.value, self._flatten(node.next))


def merge(node1, node2):
    merged = LinkedList(None)
    if node1 is None:
        return node2
    if node2 is None:
        return node1
    node1_elt = node1.head
    node2_elt = node2.head
    while node1_elt is not None or node2_elt is not None:
        if node1_elt is None:
            merged.append(node2_elt)
            node2_elt = node2_elt.next
        elif node2_elt is None:
            merged.append(node1_elt)
            node1_elt = node1_elt.next
        elif node1_elt.value <= node2_elt.value:
            merged.append(node1_elt)
            node1_elt = node1_elt.next
        else:
            merged.append(node2_elt)
            node2_elt = node2_elt.next
        return merged
''' Test merge() function'''
linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

merged = merge(linked_list, second_linked_list)
node = merged.head
while node is not None:
    # This will print 1 2 3 4 5
    print(node.value)
    node = node.next

# Lets make sure it works with a None list
merged = merge(None, linked_list)
node = merged.head
while node is not None:
    # This will print 1 3 5
    print(node.value)
    node = node.next
''' Test flatten() function'''
# Create a nested linked list with one node.
# The node itself is a simple linked list as 1-->3-->5 created previously
nested_linked_list = NestedLinkedList(Node(linked_list))

# Append a node (a linked list as 2-->4) to the existing nested linked list
nested_linked_list.append(second_linked_list)

# Call the `flatten()` function
flattened = nested_linked_list.flatten()

# Logic to print the flattened list
node = flattened.head
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    node = node.next