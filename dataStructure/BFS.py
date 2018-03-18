import types
from collections import deque


class DFS:
    queue = deque()
    graph = {}
    searched_list = []

    def __init__(self, graph: dict, check_search_condition: types.FunctionType):
        self.graph = graph
        self.check_search_condition = check_search_condition

    def search(self, criteria: str, will_search_name: str):
        queue = self.queue

        if criteria in self.searched_list:
            return False

        search_nodes = self.graph[criteria]

        if search_nodes is False:
            return False

        if type(search_nodes) is list:
            queue.extend(search_nodes)
        else:
            queue.append(search_nodes)

        while queue:
            current_search_node = queue.popleft()

            if current_search_node in self.searched_list:
                continue

            self.searched_list.append(current_search_node)

            result = self.check_search_condition(current_search_node, will_search_name)

            if result is True:
                return result

            if result is False and self.graph.get(current_search_node, False) is not False:
                queue.extend(self.graph[current_search_node])

        return False
