# 🌩️☁️⭐❤️💛💚🤍🌲🛢️🚁💧🌊🔥🏥🏪🟫🟩⬛

from map import Map
import time
import os
from helicopter import Helivopter as heli
from pynput import keyboard

TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_W, MAP_H = 10, 10

tmp = Map(MAP_H, MAP_W)
tmp.cells[0][0] = 1
tmp.cells[1][1] = 2
tmp.cells[2][2] = 3
tmp.cells[3][3] = 4
if (tmp.check_bounds(50, 5)):
    print("Ага, в пределах границ!")
tmp.generate_forest(70, 100)
tmp.generate_river(15)
tmp.generate_river(15)
tmp.generate_river(15)
tmp.generate_river(15)
tmp.generate_river(15)
tmp.generate_river(15)
tmp.generate_river(15)
tmp.generate_river(15)
# tmp.generate_river(15)
# tmp.generate_river(15)
# tmp.generate_river(15)
# tmp.generate_river(15)
# tmp.generate_river(15)
# tmp.generate_river(15)
# tmp.generate_river(15)
# tmp.generate_river(15)
# tmp.generate_river(15)
# tmp.generate_river(15)
# tmp.generate_river(15)
# tmp.generate_river(15)
tmp.cells[0][0] = 1
tmp.cells[1][1] = 2
tmp.cells[2][2] = 3
tmp.cells[3][3] = 4
# tmp.add_fire()

helic = heli(MAP_H, MAP_W)

tick = 1


MOVES_KEY = {"a":(0, -1),"d":(0, 1), "w":(-1, 0), "s":(1,0)}

def key_input(key, injected):
    global helic
    str_key = key.char.lower()
    dx, dy= MOVES_KEY[str_key][0],MOVES_KEY[str_key][1]
    print(dx,"\n\r" ,dy)
    helic.move(dx, dy)
    # keyboard.press('a')ывцфвф
    # helic.move()wasdwawda


    # print('{} released; it was {}'.format(
    #     key, 'faked' if injected else 'not faked'))
    # if key == keyboard.Key.esc:
    #     # Stop listener
    #     return False



listener = keyboard.Listener(

    on_release=key_input)
listener.start()


while True:
    os.system("cls")
    print("TICK", tick)

    helic.print_status()
    tmp.print_map(helic)
    tmp.process_helic(helic)
    tick += 1
    time.sleep(TICK_SLEEP)
    if tick % TREE_UPDATE == 0:
        tmp.gertate_tree()
    if tick % FIRE_UPDATE == 0:
        tmp.update_fires()
    if tick == 100:
        tick = 0