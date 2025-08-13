from utils import randcell
BOUNDS = "🔲"
class Helivopter:

    def __init__(self,h,w):
        rc = randcell(h,w)
        rx, ry = rc[0], rc[1]
        self.h, self.w = h, w
        self.x, self.y = rx, ry
        self.tank = 1
        self.mxtank = 4

    def move(self, dx, dy):
        nx, ny = dx + self.x, dy + self.y
        if nx >= 0 and ny >= 0 and ny < self.h and nx < self.w:
            self.x, self.y = nx, ny

    def print_status(self):
        print(BOUNDS * (self.w + 2))
        # prn_tmp = self.mxtank-self.tank
        # if (prn_tmp) >= 10:
        #     prn = "🗑️ " * (prn_tmp)
        # else:
        #     prn = "🗑️ " * (prn_tmp)
        # print("🛢️ " * self.tank, "🗑️ " * self.tank if (prn_tmp) < 10 else "🗑️  * ", prn_tmp)
        print(f"🛢️ {self.tank} / {self.mxtank}")