import time
import math
from datetime import datetime
import ANSI
import random

print("Loading module: Goosefull..")

# this is basicly Juliano's trash bin of usefull stuff


# =========================
# -------GRID  STUFF-------
# =========================

opposite_dir = {0: 2, 1: 3, 2: 0, 3: 1}  # N<->S, E<->W

def give_neighbours(grid, x, y, mode='+'):
    result = []
    if mode == '3x3':
        offsets = [(dx, dy) for dx in [-1,0,1] for dy in [-1,0,1] if not (dx==0 and dy==0)]
    elif mode == '+':
        offsets = [(0,-1),(1,0),(0,1),(-1,0)]
    
    for i, (dx, dy) in enumerate(offsets):  # N E S W
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            val = grid[nx][ny]
            if val != -1:
                result.append((val, i))
    return result

def count_neighbours(grid, x, y, mode='3x3'):
    counts = {}
    if mode == '3x3':
        offsets = [(dx, dy) for dx in [-1,0,1] for dy in [-1,0,1] if not (dx==0 and dy==0)]
    elif mode == '+':
        offsets = [(0,-1),(1,0),(0,1),(-1,0)]
    
    for dx, dy in offsets:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            val = grid[nx][ny]
            counts[val] = counts.get(val, 0) + 1
    return counts

def superposition_entropy(neighbours, all_superpos, biasses):
    '''
    neighbours acces:   neighbours[direction]       =  [neighbours]
    all_superpos acces: all_superpos                =  [ter, ter, ter, ter, ter, ter]
    biasses acces:      biasses[terrain][direction] =  [terrain, bias]
    '''
    allowed = set(all_superpos)
    if not neighbours:
        return allowed, len(allowed)

    for direction, neighbour_list in neighbours.items():
        allowed_from_dir = set()
        for neighbour_terrain in neighbour_list:
            for terrain, bias in biasses[neighbour_terrain][opposite_dir[direction]]:
                if bias > 0:
                    allowed_from_dir.add(terrain)
        allowed &= allowed_from_dir  # intersect: must be valid from ALL directions

    entropy = len(allowed)
    return allowed, entropy

def List_is_list_2D(list1, list2):
    for x in range(len(list1)):
        for y in range(len(list1[x])):
            if list1[x][y] != list2[x][y]:
                return False
    return True

def list_in_history(list, history):
    for past in history:
        if List_is_list_2D(list, past):
            return True
    return False
    
def leftover_2D(grid, search):
    count = 0
    for row in grid:
        for item in row:
            if item == search:
                count += 1
    return count

def print_grid(grid, align=4):
    height = len(grid)
    width = len(grid[0])
    print()
    print("╋━"+"━"*(align*width)+"━━╋")
    print("┃"," "*(align*width)," ┃")
    for row in range(height):
        print("┃ ", end="")
        for column in range(width):
                item = str(grid[row][column])
                print(item.rjust(align), end="")
        print("  ┃")
        print("┃"," "*(align*width)," ┃")
    print("╋━"+"━"*(align*width)+"━━╋", )

def make_grid(length,width,values= [-1]):
    if not width:
        width = length
    grid = []
    for y in range(length):
        grid.append([])
        for x in range(width):
            grid[y].append(random.choice(values))
    return grid



# =========================
# -------INFO  STUFF-------
# =========================

def info_time(asc_start, time1, asc_end, time2, message="Total time is: {difference}"):
    print("\nStarted at:",asc_start)
    print("Finished at:", asc_end)

    dt1 = datetime.fromtimestamp(time1)
    dt2 = datetime.fromtimestamp(time2)

    difference = dt2 - dt1
    print(message.format(difference = difference))

def print_set(a_set, name_only):
    if not name_only:
        for item in a_set:
            print(f"{item}: {a_set[item]}")
    else:
        for item in a_set:
            print(item)
# =========================
# -------MATH  STUFF-------
# =========================

def lerp(x, start, end):
    return round((end-start)*x*0.01, 2)

def smoothstep(x, start, end):
    t = (x - start) / (end - start)
    t = min(1, max(0, t))
    return t * t * (3 - 2 * t)

def ease_in_out_spring(x, start, end):
    if start == end:
        return 0.0

    t = (x - start) / (end - start)
    t = max(0.0, min(1.0, t))

    # damped oscillator centered at 0.5
    damping = 10
    frequency = 8 * math.pi

    if t == 0 or t == 1:
        return t

    return (
        1
        - math.exp(-damping * t)
        * math.cos(frequency * t)
    )


def credit():
    print(
        f"{ANSI.UP(1)+ANSI.CLEAR_LINE()+ANSI.C.GREEN}Loaded Module:{ANSI.C.END} Guli's {ANSI.C.PURPLE}goose{ANSI.C.BLUE}full{ANSI.C.END} stuff."
        )
credit()