import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ---------- Read the CSV ----------
# CSV should have columns: x, y, z, orientation
df = pd.read_csv("bricks_layout.csv")

# Brick size in mm (example 200x100x100, change as per your definition)
BRICK_L, BRICK_W, BRICK_H = 200, 100, 100

# ---------- Create function to draw a brick ----------
def get_brick_vertices(x, y, z, orientation):
    """Return 8 corner points of a brick at (x,y,z) with orientation."""
    if orientation == "x":
        l, w, h = BRICK_L, BRICK_W, BRICK_H
    elif orientation == "y":
        l, w, h = BRICK_W, BRICK_L, BRICK_H
    else:  # default orientation z
        l, w, h = BRICK_L, BRICK_W, BRICK_H
    
    points = [
        [x, y, z],
        [x+l, y, z],
        [x+l, y+w, z],
        [x, y+w, z],
        [x, y, z+h],
        [x+l, y, z+h],
        [x+l, y+w, z+h],
        [x, y+w, z+h]
    ]
    return points

def get_faces(points):
    return [
        [points[0], points[1], points[2], points[3]],  # bottom
        [points[4], points[5], points[6], points[7]],  # top
        [points[0], points[1], points[5], points[4]],  # front
        [points[2], points[3], points[7], points[6]],  # back
        [points[1], points[2], points[6], points[5]],  # right
        [points[0], points[3], points[7], points[4]]   # left
    ]

# ---------- Plot ----------
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

bricks = []  # store Poly3DCollection for each brick

for i, row in df.iterrows():
    points = get_brick_vertices(row['x'], row['y'], row['z'], row['orientation'])
    faces = get_faces(points)
    brick = Poly3DCollection(faces, facecolors='red', edgecolors='black', alpha=0.8, linewidths=0.3, picker=True)
    ax.add_collection3d(brick)
    bricks.append((brick, row))  # store tuple (brick artist, row info)

# Set limits (adjust as per cuboid dimensions)
ax.set_xlim([0, df['x'].max() + BRICK_L])
ax.set_ylim([0, df['y'].max() + BRICK_W])
ax.set_zlim([0, df['z'].max() + BRICK_H])
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Interactive Brick Cuboid")

# ---------- Interactivity: click to remove ----------
def on_pick(event):
    artist = event.artist
    for brick, row in bricks:
        if brick == artist:
            brick.remove()
            print(f"Removed brick at (x={row['x']}, y={row['y']}, z={row['z']}, orientation={row['orientation']})")
            plt.draw()
            break

fig.canvas.mpl_connect('pick_event', on_pick)

plt.show()
