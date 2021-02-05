class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:  # check if the value already exist
            return

        if data < self.data:  # less the value of current node
            # add data in left sub-tree
            if self.left:  # check first if your left element has some value
                self.left.add_child(data)  # recursively call the left data

            else:  # left node is empty
                self.left = BinarySearchTreeNode(data)  # add to left sub-tree

        else:
            # if greater than add to right sub-tree,
            if self.right:  # check if your right element has some value
                self.right.add_child(data)  # recursively call the right data
            else:  # right node is empty
                self.right = BinarySearchTreeNode(
                    data)  # add to right sub-tree

    # traversal techniques
    def in_order_traversal(self):
        elements = []

        # check left tree first
        if self.left:
            elements += self.left.in_order_traversal()

        # next root node
        elements.append(self.data)

        # finally right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        pass

    def pre_order_traversal(self):
        pass
    # search method

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            # val might be in left sub-tree
            if self.left:  #
                return self.left.search(val)
            else:  # it means you are in the leaf node
                return False

        if val > self.data:
            # val might be in right sub-tree
            if self.right:
                return self.right.search(val)
            else:  # it means you are in the left node
                return False

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def calculate_sum(self):
        sum = 0
        if self.left:
            sum += self.left.calculate_sum()

        sum += self.data

        if self.right:
            sum += self.right.calculate_sum()

        return sum


def build_tree(elements):  # helper function
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == "__main__":
    numbers = [5, 9, 10, 4, 11, 100]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.calculate_sum())
