class DFS:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        self.visited = []
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                if end is None:
                    self.graph_dict[start] = []
                else:
                    self.graph_dict[start] = [end]

    def depth_first_search(self, start_point, path=[]):
        if start_point not in self.visited:
            self.visited.append(start_point)
            for node in self.graph_dict[start_point]:
                return self.depth_first_search(node, self.visited)
            return self.visited


if __name__ == '__main__':
    routes = [
        ('Mumbai', 'Paris'),
        ('Mumbai', 'Dubai'),
        ('Paris', 'Dubai'),
        ('Paris', 'New York'),
        ('Dubai', 'New York'),
        ('New York', 'Toronto'),
        ('Toronto', None)
    ]

    g = DFS(routes)
    # print(g.graph_dict)
    print(g.depth_first_search('Mumbai'))
