import heapq

F_X, G_X_ONLY, H_X_ONLY = 0, 1, 2

MAP = {
    "arad": (("sibiu", 140), ("zerind", 75), ("timisoara", 118)),
    "bucharest": (("pitesti", 101), ("fagaras", 211), ("urziceni", 85), ("giurgiu", 90)),
    "craiova": (("dobreta", 120), ("pitesti", 138), ("rimnicu vilcea", 146)),
    "dobreta": (("mehadia", 75), ("craiova", 120)),
    "eforie": (("hirsova", 88), ),
    "fagaras": (("sibiu", 99), ("bucharest", 211)),
    "giurgiu": (("bucharest", 90), ),
    "hirsova": (("urziceni", 98), ("eforie", 88)),
    "iasi": (("neamt", 87), ("vaslui", 92)),
    "lugoj": (("timisoara", 111), ("mehadia", 70)),
    "mehadia": (("lugoj", 70), ("dobreta", 75)),
    "neamt": (("iasi", 87), ),
    "oradea": (("zerind", 71), ("sibiu", 151)),
    "pitesti": (("rimnicu vilcea", 97), ("bucharest", 101)),
    "rimnicu vilcea": (("sibiu", 80), ("pitesti", 97)),
    "sibiu": (("arad", 140), ("oradea", 151), ("fagaras", 99), ("rimnicu vilcea", 80)),
    "timisoara": (("arad", 118), ("lugoj", 111)),
    "urziceni": (("bucharest", 85), ("vaslui", 142), ("hirsova", 98)),
    "vaslui": (("iasi", 92), ("neamt", 87)),
    "zerind": (("arad", 75), ("oradea", 71)),
    "b": ()
}

STRAIGHT_LINE_DISTANCE = {
    "arad": 100, "bucharest": 0, "craiova": 160, "dobreta": 242, "eforie": 161, "fagaras": 176, "giurgiu": 77,
    "hirsova": 151, "iasi": 266, "lugoj": 244, "mehadia": 241, "neamt": 234, "oradea": 380, "pitesti": 10,
    "rimnicu vilcea": 193, "sibiu": 253, "timisoara": 329, "urziceni": 80, "vaslui": 199, "zerind": 374, "b": 1001
}

def aStar(start, finish, mode):
    s, min_heap, loop = set(), [(0, ["arad"])], 0
    heapq.heapify(min_heap)
    try:
        while True:
            loop += 1
            current_min_path = heapq.heappop(min_heap)
            current_cost = current_min_path[0]
            last_node = current_min_path[1][-1]
            if last_node in s:
                continue
            if last_node == finish:
                return loop, current_min_path
            s.add(last_node)
            for next_node in MAP[last_node]:
                if mode == F_X:
                    next_cost = current_cost + STRAIGHT_LINE_DISTANCE[next_node[0]] + next_node[1]
                elif mode == G_X_ONLY:
                    next_cost = current_cost + next_node[1]
                else:
                    next_cost = STRAIGHT_LINE_DISTANCE[next_node[0]]
                heapq.heappush(min_heap, (next_cost, current_min_path[1] + [next_node[0]]))
    except IndexError:
        return loop, (0, "No Solution")

print("Shortest path using A* with f(x) = g(x) + h(x): ")
loop_time, shortest_path = aStar("arad", "bucharest", F_X)
print(shortest_path[1], ", loop time: ", loop_time)

print("Shortest path using A* with f(x) = g(x): ")
loop_time, shortest_path = aStar("arad", "bucharest", G_X_ONLY)
print(shortest_path[1], ", loop time: ", loop_time)

print("Shortest path using A* with f(x) = h(x): ")
loop_time, shortest_path = aStar("arad", "bucharest", H_X_ONLY)
print(shortest_path[1], ", loop time: ", loop_time)