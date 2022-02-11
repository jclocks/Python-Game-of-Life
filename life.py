#!/usr/bin/python3

import random
import time
import os

LIVE = "@"
DEAD = "O"
BLANK = " "

# Edit me to change desired height/width, and update rate (seconds).
height = 24
width = 80
seconds = 0.5

# Populate grid
grid = []
for x in range(height):
    grid.append([])
    for y in range(width):
        if random.randint(0, 1) == 1:
            grid[x].append(LIVE)
        else:
            grid[x].append(BLANK)

# Loop the game indefinitely. Game can be stopped via interrupt. (Ctrl+c)
try:
    while True:

        # Display grid
        os.system("clear")
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                print(grid[x][y], end="")
            print()

        # Evaluate grid
        new_grid = []

        for x in range(len(grid)):
            new_grid.append([])
            for y in range(len(grid[x])):
                live_count = 0

                # Evaluate how many live cells surround the current cell.
                try:
                    if grid[x + 1][y] == LIVE:
                        live_count += 1
                except IndexError:
                    pass
                try:
                    if grid[x - 1][y] == LIVE:
                        live_count += 1
                except IndexError:
                    pass
                try:
                    if grid[x][y + 1] == LIVE:
                        live_count += 1
                except IndexError:
                    pass
                try:
                    if grid[x][y - 1] == LIVE:
                        live_count += 1
                except IndexError:
                    pass
                try:
                    if grid[x + 1][y + 1] == LIVE:
                        live_count += 1
                except IndexError:
                    pass
                try:
                    if grid[x + 1][y - 1] == LIVE:
                        live_count += 1
                except IndexError:
                    pass
                try:
                    if grid[x - 1][y - 1] == LIVE:
                        live_count += 1
                except IndexError:
                    pass
                try:
                    if grid[x - 1][y + 1] == LIVE:
                        live_count += 1
                except IndexError:
                    pass

                # Determine if cell should be alive or dead.
                if (live_count == 2 or live_count == 3) and grid[x][y] == LIVE:
                    new_grid[x].append(LIVE)
                elif live_count == 3 and (grid[x][y] == DEAD
                                          or grid[x][y] == BLANK):
                    new_grid[x].append(LIVE)
                elif grid[x][y] == LIVE:
                    new_grid[x].append(DEAD)
                else:
                    new_grid[x].append(BLANK)

        # Overwrite grid
        grid = new_grid
        time.sleep(seconds)

# Suppress keyboard interrupt exception.
except KeyboardInterrupt:
    pass
