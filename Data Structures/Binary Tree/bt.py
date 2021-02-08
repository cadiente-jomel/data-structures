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
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
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

    def delete(self, val):
        if val < self.data:  # check if val is less than the current node
            if self.left:  # check if left node exist
                # call left node delete method recursively
                self.left = self.left.delete(val)
        elif val > self.data:  # val is greater than the current node
            if self.right:  # right node exist
                # call right node delete method recursively
                self.right = self.right.delete(val)
        else:  # it means the val and current node is equal
            if self.left is None and self.right is None:  # if the left and right is none return None
                return None

            if self.left is None:  # if left is none return right node
                return self.right

            if self.right is None:  # if right is none return left node
                return self.left

            # if both left and right node are not empty
            # min_val = self.right.find_min()  # get the minimum value to right node
            # self.data = min_val  # replace the current node with the min value
            # and finally remove the min val to its current position
            # self.right = self.right.delete(min_val)

            max_val = self.left.find_max()  # get the maximum value to left node
            self.data = max_val  # replace the current node with the max value
            self.left = self.left.delete(max_val)

        return self


def build_tree(elements):  # helper function
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == "__main__":

    numbers = [15, 12, 7, 14, 27, 20, 23, 88]

    numbers_tree = build_tree(numbers)
    print("Input numbers:", numbers)
    print("Min:", numbers_tree.find_min())
    print("Max:", numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())
    print("In order traversal:", numbers_tree.in_order_traversal())
    print("Pre order traversal:", numbers_tree.pre_order_traversal())
    print("Post order traversal:", numbers_tree.post_order_traversal())
    print("Delete:", numbers_tree.delete(15))
    print("In order traversal:", numbers_tree.in_order_traversal())
