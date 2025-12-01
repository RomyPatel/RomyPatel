import csv

WIDTH = 40
HEIGHT = 20

grid = [['⬜' for _ in range(WIDTH)] for _ in range(HEIGHT)]

with open("data/strokes.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        x = int(row["x"])
        y = int(row["y"])
        if 0 <= x < WIDTH and 0 <= y < HEIGHT:
            grid[y][x] = "⬛"

print("# 🎨 GitHub Profile Paint Game\n")
print("Submit a GitHub Issue to draw on this board!\n")

for row in grid:
    print("".join(row))
