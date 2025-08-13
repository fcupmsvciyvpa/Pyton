from utils import randbool
from utils import randcell
from utils import randcell2


CELL_TYPES = "🟫🌲🌊🏥🏪🔥"

BOUNDS = "🔲"

class Map:

    def generate_river(self, l):
        rc = randcell(self.h, self.w)
        rx, ry = rc[0], rc[1]
        # rxs, rys = rc[0], rc[1]
        r2 = {}
        self.cells[rx][ry] = 2  # Set river start
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if  self.check_bounds(rx2, ry2):
                    if self.cells[rx2][ry2] == 0:
                        self.cells[rx][ry] = 2
                        rx, ry = rx2, ry2
                        l -= 1
                        r2.clear()
                    elif self.cells[rx2][ry2] == 2:
                        rx, ry = rx2, ry2
                    else:
                        rx, ry = rx2, ry2
                        l -= 1


    def generate_forest(self, r , mxr):
        for ci in range(self.h):
            for ri in range(self.w):
                if randbool(r, mxr):
                    self.cells[ci][ri] = 1

    def gertate_tree(self):
        c = randcell(self.h, self.w)
        cx, cy = c[0], c[1]
        if (self.check_bounds(cx, cy) and self.cells[cx][cy] == 0):
            self.cells[cx][cy] = 1
    
    def print_map(self, heli):
        print(BOUNDS * (self.w + 2))
        for ri in range(self.h):
            print(BOUNDS, end="")
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if ri == heli.x and ci == heli.y:
                    print("🚁",  end="")
                else:
                    print(CELL_TYPES[cell], end="")
            print(BOUNDS)
        print(BOUNDS * (self.w + 2))

    # def check_unit(self, u):
    #     for ri in range(self.h):
    #         for ci in range(self.w):
    #             if self.cells[ri][ci] == u:
    #                 return True 
    
    def add_fire(self):
        n = self.h + self.w
        while n > 0:
            c = randcell(self.h,self.w)
            cx, cy = c[0], c[1]
            if self.cells[cx][cy] == 1:
                self.cells[cx][cy] = 5
                n -= self.h + self.w
            else:
                n -= 1

    def update_fires(self):
        for ri in range(self.h):
            for ci in range(self.w):
                if self.cells[ri][ci] == 5:
                    self.cells[ri][ci] = 0
                    self.add_fire()
        # else:
        for rci in range(10):
            self.add_fire()


    def check_bounds(self, x, y):
        if (x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        return True

    def __init__(self, w, h):
        self.w = w
        self.h = h
        # Initialize a grid with an extra border of 0s
        self.cells = [[0 for i in range(w)] for j in range(h)]

    def process_helic(self, helic):
        if self.cells[helic.x][helic.y] == 2:
            helic.tank = helic.mxtank
        elif self.cells[helic.x][helic.y] == 5 and helic.tank > 0:
            self.cells[helic.x][helic.y] = 1
            helic.tank -= 1
        elif self.cells[helic.x][helic.y] == 4:
            helic.mxtank += 1



print(60%50)