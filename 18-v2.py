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
"""


def create_list_from_triangle_string(triangle_string):
    triangle = []
    for row in map(lambda x: x.split(" "), triangle_string.strip().split("\n")):
        triangle.append(map(int, row))
    return triangle


def convert_triangle_to_graph(triangle_string):
    # WIP
    triangle = create_list_from_triangle_string(triangle_string)
    vertex_mapping = {}
    i = 1
    x = y = 0
    for row in triangle:
        for cell in row:
            vertex_mapping[i] = [x,y]
            y += 1
            i += 1
        x += 1
    print(vertex_mapping)




def get_next_max(q):
    max_weight = 0
    next_v = 0
    for v, edge_weight in graph[q].items():
        if edge_weight > max_weight:
            max_weight = edge_weight
            next_v = v
    return next_v


graph = {
    0: {1: 75},
    1: {2: 95, 3: 64},
    2: {4: 17, 5: 47},
    3: {5: 47, 6: 82},
    4: {7: 18, 8: 35},
    5: {8: 35, 9: 87},
    6: {9: 87, 10: 10},
    7: {11: 0},
    8: {11: 0},
    9: {11: 0},
    10: {11: 0},
    11: {}
}

def dijkstra(graph, source, target):
    source = 0
    target = 11

    q = list()
    dist = {}
    prev = {}

    for v, edge in graph.items():
        dist[v] = 0
        prev[v] = None
        q.append(v)

    dist[source] = 0

    while q:
        u = get_next_max(q[0])
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

#print dijkstra(graph, 0, 11)

convert_triangle_to_graph(triangle_string)