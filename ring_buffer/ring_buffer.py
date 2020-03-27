from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
        else:
            # reaching capacity or last item in the list
            if self.current == None or self.current.next == None:
                # use the head
                self.current = self.storage.head
            else:
                # use the next of current
                self.current = self.current.next
            self.current.value = item

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        node = self.storage.head
        while node != None:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents


rb = RingBuffer(5)
rb.append('a')
rb.append('b')
rb.append('c')
rb.append('d')
rb.append('e')
# rb.append('f')
# rb.append('g')
# rb.append('h')

print(rb.get())

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
