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

    def breadth_first_search(self, starting_vertex):
        visited = []
        queue = [starting_vertex]

        path = []

        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node not in visited:
                visited.append(current_node)
                path.append(current_node)
                for node in self.graph_dict[current_node]:
                    if node not in visited:
                        queue.append(node)
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
    print(g.breadth_first_search('Paris'))
