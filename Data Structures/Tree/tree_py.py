# # general tree
# class Tree:
#     def __init__(self, data):
#         self.data = data
#         self.children = []
#         self.parent = None

#     def add_child(self, child):
#         child.parent = self
#         self.children.append(child)

#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level += 1
#             p = p.parent
#         return level

#     def print_tree(self):
#         spaces = ' ' * self.get_level() * 3
#         prefix = spaces + '|___' if self.parent else ' '
#         print(prefix + self.data)
#         if self.children:
#             for child in self.children:
#                 child.print_tree()


# def build_product_tree():
#     root = Tree('Electronics')

#     laptop = Tree('Laptop')
#     laptop.add_child(Tree('Mac'))
#     laptop.add_child(Tree('Surface'))
#     laptop.add_child(Tree('Thinkpad'))

#     cellphone = Tree('Cell Phone')
#     cellphone.add_child(Tree('iPhone'))
#     cellphone.add_child(Tree('Google Pixel'))
#     cellphone.add_child(Tree('Vivo'))

#     tv = Tree('TV')
#     tv.add_child(Tree('Samsung'))
#     tv.add_child(Tree('LG'))

#     root.add_child(laptop)
#     root.add_child(cellphone)
#     root.add_child(tv)

#     return root


# if __name__ == "__main__":
#     root = build_product_tree()
#     root.print_tree()
#     pass

import re


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, data):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|____' if self.parent else ''

        _string = re.split('[()]', self.data)
        if data == 'designation':
            print(prefix + _string[1])
        elif data == 'name':
            print(prefix + _string[0].rstrip())
        elif data == 'both':
            print(prefix + self.data)
        else:
            print('unabled to recognized printing method')
            return

        for child in self.children:
            child.print_tree(data)

    def print_per_level(self, level):
        if self.get_level() > level:
            return

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|____' if self.parent else ''

        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_per_level(level)


def build_product_tree():
    ceo = TreeNode('Nilupol (CEO)')

    cto = TreeNode('Chinmay (CTO)')
    infra_head = TreeNode('Vishwa (Infrastructure Head)')
    infra_head.add_child(TreeNode('Dhaval (Cloud Manager)'))
    infra_head.add_child(TreeNode('Abhijit (App Manager)'))
    cto.add_child(infra_head)
    cto.add_child(TreeNode('Aamir (Application Head)'))

    hr_head = TreeNode('Gels (HR Head)')
    hr_head.add_child(TreeNode('Peter (Recruitment Manager)'))
    hr_head.add_child(TreeNode('Waqas (Policy Manager)'))

    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo


if __name__ == '__main__':
    root = build_product_tree()

    # root.print_tree('designation')
    root.print_per_level(1)
    pass
