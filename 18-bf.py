
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

triangle_string = """
3
7 4
2 4 6
8 5 9 3
"""

class BruteForce:


    paths = []

    def __init__(self, triangle_string):
        self.triangle = self.create_list_from_triangle_string(triangle_string)

    def main(self):
        return self.get_all_paths()
        return self.find_max_path()

    def find_max_path(self):
        max_sum = 0
        max_path = self.paths[0]
        for path in self.paths:
            sum_of_path = self.get_sum_of_path(path)
            if sum_of_path > max_sum:
                max_sum = sum_of_path
                max_path = path

        route = []
        for y, x in enumerate(max_path[::-1]):
            route.append(self.triangle[y][x])
        return max_sum, max_path[::-1], route,


    @staticmethod
    def create_list_from_triangle_string(triangle_string):
        triangle = []
        for row in map(lambda x: x.split(" "), triangle_string.strip().split("\n")):
            triangle.append(map(int, row))
        return triangle

    def get_all_paths(self):
        i = 1
        next_path = [0] * len(self.triangle)

        while next_path is not None:
            self.paths.append(next_path)
            next_path = self.get_next_path(next_path)
            i += 1

        return self.paths

    @staticmethod
    def get_next_path(path):
        next_path = path[:]
        path_length = len(path)
        i = 0
        while path[i] == path[i + 1] and not (i > 1 and i < path_length and path[i - 1] == path[i]):
            i +=1
        increment = i - 1
        next_path[increment] += 1

        return next_path

        for k, i in enumerate(path):
            if k + 1 >= path_length:
                return None
            # while i + 1 == path[k + 1] + 1 and k < path_length - 1:


            if i + 1 == path[k + 1] + 1:

                next_path[k] = i + 1
                return next_path



    def get_sum_of_path(self, path):
        sum_of_path = 0
        for y, x in enumerate(path[::-1]):
            sum_of_path += self.triangle[y][x]
        return sum_of_path



bf = BruteForce(triangle_string)
print bf.get_next_path([1,1,0,0])


#print(brute_force(triangle_string))


#print(next_path([0] * 3))