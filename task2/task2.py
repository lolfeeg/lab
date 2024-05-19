from pathlib import Path
from math import sqrt
data, coordinates = Path(input()), Path(input())
with open(data, 'r', encoding='utf-8') as file:
    coord_x0, coord_y0 = [int(cyc) for cyc in file.readline().split()]
    radius = int(file.readline())
with open(coordinates, 'r', encoding='utf-8') as file:
    for coord in file:
        coord_x, coord_y = [int(cyc) for cyc in coord.split()]
        distance = sqrt((coord_x - coord_x0)**2 + (coord_y - coord_y0)**2)
        if distance < radius:
            print(1)
        elif distance == radius:
            print(0)
        else:
            print(2)
