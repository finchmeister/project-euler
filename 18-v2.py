"""
https://medium.com/basecs/finding-the-shortest-path-with-a-little-help-from-dijkstra-613149fbdc8e
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

"""
triangle_string = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

sub_triangle = """
75
95 64
17 47 82
18 35 87 10
"""

sub_triangle_2 = """
3
7 4
2 4 6
8 5 9 3
"""

def compute_max_path_from_triange(triangle_string):
    triangle = create_list_from_triangle_string(triangle_string)
    graph = convert_triangle_to_graph(triangle)
    source_vertex = 0
    target_vertex = max(graph, key=int)
    dijkstra_result = dijkstra(graph, source_vertex, target_vertex)
    print(graph)
    print(dijkstra_result[0])
    print(dijkstra_result[1])
    return get_max_distance_from_dijkstra(dijkstra_result, graph)


def create_list_from_triangle_string(triangle_string):
    triangle = []
    for row in map(lambda x: x.split(" "), triangle_string.strip().split("\n")):
        triangle.append(map(int, row))
    return triangle


def convert_triangle_to_graph(triangle):
    vertex = 1
    x = 0
    y = 1
    mapping = {0: {0: 0}}
    for row in triangle:
        mapping_x = {}
        for cell in row:
            mapping_x[x] = vertex
            vertex += 1
            x += 1
        mapping[y] = mapping_x
        x = 0
        y += 1

    vertex_max = vertex
    graph = {}

    for y, mapping_x in mapping.items():
        next_y = y + 1
        next_level = mapping.get(next_y)
        for x, vertex in mapping_x.items():
            graph_next = {}
            if next_level is not None:
                x1 = x
                x2 = x + 1
                if next_level.get(x1) is not None:
                    next_vertex_1 = mapping[next_y][x1]
                    graph_next[next_vertex_1] = triangle[y][x1]

                if next_level.get(x2) is not None:
                    next_vertex_2 = mapping[next_y][x2]
                    graph_next[next_vertex_2] = triangle[y][x2]
                graph[vertex] = graph_next
            else:
                graph[vertex] = {vertex_max: 0}
    graph[vertex_max] = {}
    return graph


def get_next_max(q, graph):
    max_weight = 0
    next_v = 0
    for v, edge_weight in graph[q].items():
        if edge_weight > max_weight:
            max_weight = edge_weight
            next_v = v
    return next_v


# graph = {
#     0: {1: 75},
#     1: {2: 95, 3: 64},
#     2: {4: 17, 5: 47},
#     3: {5: 47, 6: 82},
#     4: {7: 18, 8: 35},
#     5: {8: 35, 9: 87},
#     6: {9: 87, 10: 10},
#     7: {11: 0},
#     8: {11: 0},
#     9: {11: 0},
#     10: {11: 0},
#     11: {}
# }

def dijkstra(graph, source, target):
    q = list()
    dist = {}
    prev = {}

    for v, edge in graph.items():
        dist[v] = 0
        prev[v] = None
        q.append(v)

    dist[source] = 0

    while q:
        u = get_next_max(q[0], graph)
        del q[0]
        if u == target:
            return dist, prev

        neighbours = graph[u].items()
        for v, length in neighbours:
            alt = dist[u] + length
            if alt > dist[v]:
                dist[v] = alt
                prev[v] = u

    return dist, prev


def get_max_distance_from_dijkstra(dijkstra_result, graph):
    dijkstra_prev = dijkstra_result[1]
    target_vertex = int(max(dijkstra_prev, key=int))
    current_vertex = target_vertex
    max_dist = 0
    while current_vertex > 0:
        prev_vertex = dijkstra_prev[current_vertex]
        max_dist += graph[prev_vertex][current_vertex]
        current_vertex = prev_vertex
    return max_dist


print compute_max_path_from_triange(triangle_string)