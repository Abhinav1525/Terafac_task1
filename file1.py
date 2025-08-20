import csv

# Brick dimensions (mm)
BRICK_L, BRICK_W, BRICK_H = 200, 100, 100

# Cuboid dimensions (mm) from best fit
L, W, H = 3400, 4000, 5600
WALL = 200  # wall thickness

filename = "bricks_layout.csv"

def is_inside_hollow(x, y, z):
    """Check if the brick lies fully inside hollow space."""
    return (
        WALL <= x < L - WALL and
        WALL <= y < W - WALL and
        WALL <= z < H - WALL
    )

bricks = []
brick_id = 1

# Generate brick positions
for x in range(0, L, BRICK_L):
    for y in range(0, W, BRICK_W):
        for z in range(0, H, BRICK_H):
            if is_inside_hollow(x, y, z):
                continue
            bricks.append([
                brick_id, x, y, z, BRICK_L, BRICK_W, BRICK_H, "X-aligned"
            ])
            brick_id += 1

print(f"Total bricks placed: {len(bricks)}")

# Save to CSV
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["brick_id", "x", "y", "z", "length", "width", "height", "orientation"])
    writer.writerows(bricks)

print(f"Brick layout saved to {filename}")
