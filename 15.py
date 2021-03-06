"""
Starting in the top left corner of a 2*2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20*20 grid?
"""


class LatticePaths:

    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.no_of_paths = 0
        self.routes = []

    def get_next_available_points(self, point):
        available_points = []
        across_point = (point[0] + 1, point[1])
        if across_point[0] <= self.grid_size:
            available_points.append(across_point)
        down_point = (point[0], point[1] + 1)
        if down_point[1] <= self.grid_size:
            available_points.append(down_point)
        return available_points

    # WIP
    def compute_no_of_paths(self, route):
        last_point = route[-1]
        next_points = self.get_next_available_points(last_point)
        for next_point in next_points:
            route.append(next_point)
            self.compute_no_of_paths(route)
        else:
            if route not in self.routes:
                self.routes.append(route)
            return

    def get_no_of_paths(self):
        self.compute_no_of_paths([(0,0)])
        return len(self.routes)


lp = LatticePaths(2)

# Not correct
print(lp.get_no_of_paths())
