import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s - %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next_node = next

    # def get_next(self):
    #     return self.next_node

    # def set_next(self, _next):
    #     self.next_node = _next

    # def get_data(self):
    #     return self.data

    # def set_data(self, _data):
    #     self.data = _data


# add, remove, get_size, find
class LinkedList:
    def __init__(self, root=None):
        self.root = root

    def add_to_beginning(self, _data):
        node = Node(_data, self.root)
        self.root = node

    def add_at_end(self, _data):
        if self.root is None:
            self.root = Node(_data, None)
            return

        itr = self.root
        while itr.next_node:
            itr = itr.next_node

        itr.next_node = Node(_data, None)

    def print_linked_list(self) -> str:
        if self.root is None:
            logger.warning('Linked list is empty')
            return

        itr = self.root
        linked_list_str = ''
        while itr:
            linked_list_str += str(itr.data) + '-->'
            itr = itr.next_node
        logger.info(linked_list_str)

    def insert_list_values(self, _list_val):
        self.root = None
        for _curr_data in _list_val:
            self.add_at_end(_curr_data)

    def get_length(self) -> int:
        count = 0
        itr = self.root
        while itr:
            count += 1
            itr = itr.next_node
        return count

    def remove_at(self, index: int):
        if index < 0 or index > self.get_length():
            raise IndexError('Index out of bounds')

        if index == 0:
            self.root = self.root.next_node
            return

        count = 0
        itr = self.root
        while itr:
            if count == index - 1:
                itr.next_node = itr.next_node.next_node
                break

            itr.next_node
            count += 1

    def insert_at(self, index: int, val):
        if index < 0 or index > self.get_length():
            raise IndexError('Index out of bounds')

        if index == 0:
            self.add_to_beginning(val)
            return

        itr = self.root
        count = 0

        while itr:
            if count == index - 1:
                node = Node(val, itr.next_node)
                itr.next_node = node
                break
            count += 1
            itr = itr.next_node


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_list_values(['red', 'pink', 'black', 'grey'])
    linked_list.insert_at(0, 'cyan')
    linked_list.insert_at(2, 'purple')
    linked_list.print_linked_list()
    linked_list.remove_at(2)
    linked_list.print_linked_list()
    logger.info(
        f'number of elements in a linked list {linked_list.get_length()}')
