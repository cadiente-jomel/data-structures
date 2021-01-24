import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s - %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)


class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_to_beginning(self, _data):
        if self.head is None:
            self.tail = self.head = Node(_data, None, None)
            return
        node = Node(_data, self.head, None)
        self.head = node
        self.head.next.prev = self.head

    def add_to_end(self, _data):
        if self.head is None:
            self.tail = self.head = Node(_data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(_data, None, self.tail)
        self.tail = itr.next

    def insert_list_val(self, _list_val: list):
        """
            This will remove the current linked list and replace 
            it with the value you pass to the parameter
        """
        self.head = None
        for curr_data in _list_val:
            self.add_to_end(curr_data)

    def get_length(self) -> int:
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count

    def remove_at(self, index: int):
        if index < 0 or index > self.get_length():
            raise IndexError('Index out of bounds')

        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                itr.next.prev = itr
                # itr.next.prev = itr.next.next.prev
                break
            count += 1
            itr = itr.next

    def insert_at(self, index: int, val):
        if index < 0 or index > self.get_length():
            raise IndexError('Index out of bounds')

        if index == 0:
            self.add_to_beginning(val)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(val, itr.next, itr)
                itr.next.prev = node
                itr.next = node
            count += 1
            itr = itr.next

    def print(self):
        if self.head is None:
            logger.warning('Linked list is empty')
            return

        itr = self.head
        linked_list_str = ''
        while itr:
            linked_list_str += str(itr.data) + '-->'
            itr = itr.next
        logger.info(linked_list_str)


if __name__ == '__main__':
    ll = LinkedList()
    ll.add_to_end(20)
    ll.add_to_beginning(5)
    ll.add_to_beginning(10)
    ll.add_to_beginning(6)
    ll.insert_at(1, 7)
    ll.insert_at(0, 11)
    ll.add_to_beginning(30)
    # ll.remove_at(1)
    ll.print()
    ll.get_length()
