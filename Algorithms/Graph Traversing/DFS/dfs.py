class DFS:
    """
    I used directed graph here
    """

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

    def iter_dfs(self, vertex):
        visited_nodes = []
        stack = [vertex]

        path = []

        while len(stack) > 0:
            v = stack.pop()
            if v not in visited_nodes:
                visited_nodes.append(v)
                path.append(v)
                for neighbour in self.graph_dict[v]:
                    if neighbour not in visited_nodes:
                        stack.append(neighbour)
        return path


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
    # print(g.depth_first_search('Mumbai'))
    print(g.iter_dfs('Mumbai'))
