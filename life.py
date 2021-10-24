#!/usr/bin/python3

import random, time, os, sys

if "--help" in sys.argv:
	print("Conway's Game of Life: Terminal Version by jclocks (https://github.com/jclocks/Python-Game-of-Life)\n\nUse: python3 life.py\n\nArguments:\n\t--help: Display this.")
	sys.exit()

LIVE = "@"
DEAD = "O"
BLANK = " "

# TODO: Default to getting the terminal size.
# Accept arguments to specify the terminal size.
width = os.get_terminal_size()[0]
height = os.get_terminal_size()[1]
seconds = 0.25

# Populate grid
grid = []

for x in range(height):
	grid.append([])
	for y in range(width):
		#print("Debug:\nX: " + str(x) + "\nY: " + str(y))

		if random.randint(0, 1) == 1:
			grid[x].append(LIVE)
		else:
			grid[x].append(BLANK)

# GAME LOOP

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

			# TODO: Make this suck less
			# Evaluate how many live cells surround the current cell.
			try:
				if grid[x + 1][y] == LIVE:
					live_count += 1
			except:
				pass
			try:
				if grid[x - 1][y] == LIVE:
					live_count += 1
			except:
				pass
			try:
				if grid[x][y + 1] == LIVE:
					live_count += 1
			except:
				pass
			try:
				if grid[x][y - 1] == LIVE:
					live_count += 1
			except:
				pass
			try:
				if grid[x + 1][y + 1] == LIVE:
					live_count += 1
			except:
				pass
			try:
				if grid[x + 1][y - 1] == LIVE:
					live_count += 1
			except:
				pass
			try:
				if grid[x - 1][y - 1] == LIVE:
					live_count += 1
			except:
				pass
			try:
				if grid[x - 1][y + 1] == LIVE:
					live_count += 1
			except:
				pass

			# Determine if cell should be alive or dead.
			if (live_count == 2 or live_count == 3) and grid[x][y] == LIVE:
				new_grid[x].append(LIVE)
			elif live_count == 3 and (grid[x][y] == DEAD or grid[x][y] == BLANK):
				new_grid[x].append(LIVE)
			elif grid[x][y] == LIVE:
				new_grid[x].append(DEAD)
			else:
				new_grid[x].append(BLANK)

	# Overwrite grid
	grid = new_grid
	time.sleep(seconds)