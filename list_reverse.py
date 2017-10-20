
class Node:

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:

    def __init__(self):

        self.head = None

    def add(self, value):

        t = Node(value, self.head)
        self.head = t

    def reverse(self):

        current_node = self.head
        prev_node = None
        while current_node:

            next_node = current_node.next
            current_node.next = prev_node

            prev_node = current_node
            current_node = next_node

        self.head = prev_node

    def reverse_recursive(self):

        if self.head is None:
            return

        def do(curr, prev):

            if curr is None:
                self.head = prev
                return

            next = curr.next
            curr.next = prev

            do(next, curr)

        do(self.head, None)

    def __str__(self):
        result = ""
        node = self.head
        while node:

            result += str(node.value) + " > "
            node = node.next

        result += "None"

        return result


if __name__ == "__main__":

    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)

    print str(ll)

    ll.reverse_recursive()

    print "reversed: %s" % str(ll)

