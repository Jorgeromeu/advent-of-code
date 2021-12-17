class Probe:
    x: int
    y: int
    x_vel: int
    y_vel: int

    def __init__(self, x, y, x_vel, y_vel):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel

    def step(self):
        self.x += self.x_vel
        self.y += self.y_vel

        if self.x_vel > 0:
            self.x_vel -= 1
        elif self.x_vel < 0:
            self.x_vel += 1

        self.y_vel -= 1

    def inside(self, x_min, x_max, y_min, y_max) -> bool:
        return x_min <= self.x <= x_max and y_min <= self.y <= y_max

if __name__ == "__main__":

    # example
    xmin, xmax, ymin, ymax = 20, 30, -10, -5

    # mine
    # xmin, xmax, ymin, ymax = 34, 67, -215, -186

    # pav
    # xmin, xmax, ymin, ymax = 124, 174, -123, -86

    global_max_y = 0

    for xvel in range(1000):
        for yvel in range(1000):

            probe = Probe(0, 0, xvel, yvel)
            max_height = 0

            while probe.x <= xmax and probe.y >= ymin:

                probe.step()

                max_height = max(max_height, probe.y)

                if probe.inside(xmin, xmax, ymin, ymax):
                    global_max_y = max(max_height, global_max_y)
                    break

    print(global_max_y)
