"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

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


class MaximumPathSum:

    def __init__(self, triangle_string):
        self.triangle_string = triangle_string
        self.triangle = MaximumPathSum.create_list_from_triangle_string(triangle_string)
        self.no_of_rows = len(self.triangle)
        self.path = []

    @staticmethod
    def create_list_from_triangle_string(triangle_string):
        triangle = []
        for row in map(lambda x: x.split(" "), triangle_string.strip().split("\n")):
            triangle.append(map(int, row))
        return triangle

    def get_max_path(self):
        x = y = 0
        self.path.append(self.triangle[x][y])
        while x < self.no_of_rows - 1:
            a = self.triangle[x+1][y]
            b = self.triangle[x+1][y+1]
            x += 1
            if a > b:
                self.path.append(a)
            else:
                self.path.append(b)
                y += 1
        return self.path

    def get_max_path_sum(self):
        return sum(self.get_max_path())

    def get_next_points(self, x, y):
        x1 = x2 = x + 1
        y1 = y
        y2 = y + 1
        if x1 < self.no_of_rows:
            return (x1, y1), (x2, y2)

    def brute_force_max_length_path_length_n(self, n, path, complete_paths):
        if len(path) < n:
            points = self.get_next_points(path[-1][0], path[-1][1])
            for point in points:
                path.append(point)
                self.brute_force_max_length_path_length_n(n - 1, path, complete_paths)
        return complete_paths.append(path)

    def get_sum_from_path(self, path):
        x = 0
        for point in path:
            x += self.triangle[point[0]][point[1]]
        return x

    #def search_max_path(self, x, y):


triangle = """
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




#print(MaximumPathSum(triangle).get_next_points(20,10))

print MaximumPathSum(triangle).brute_force_max_length_path_length_n(2, [(0, 0)], [])