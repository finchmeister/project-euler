"""
Starting in the top left corner of a 2*2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20*20 grid?
"""


class LatticePaths:

    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.no_of_paths = 0

    def get_next_available_points(self, point):
        available_points = []
        across_point = (point[0] + 1, point[1])
        if across_point[0] <= self.grid_size:
            available_points.append(across_point)
        down_point = (point[0], point[1] + 1)
        if down_point[1] <= self.grid_size and down_point[1] <= down_point[0]:
            available_points.append(down_point)
        return available_points

    # WIP
    def find_no_of_paths(self, point=(0, 0)):
        while point:
            points = self.get_next_available_points(point)
            self.no_of_paths += len(points)
            for point in points:
                self.find_no_of_paths(point)
            else:
                return


lp = LatticePaths(20)


print lp.find_no_of_paths()
