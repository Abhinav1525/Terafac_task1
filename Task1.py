# Brick details
BRICK_SIZE = (200, 100, 100)  # mm
BRICK_VOL = 200*100*100
TOTAL_BRICKS = 10000
wall_tickness = 200

def wall_volume(L, W, H):
    outer = L * W * H
    inner = (L- 2*wall_tickness) * (W - 2*wall_tickness) * (H - 2*wall_tickness)
    return outer - inner

best = None
for L in range(2000, 20000, 200):   # multiples of brick dimensions
    for W in range(2000, 20000, 200):
        for H in range(2000, 20000, 200):
            wall_vol = wall_volume(L, W, H)
            bricks_needed = wall_vol // BRICK_VOL
            if bricks_needed == TOTAL_BRICKS:
                if not best or L*W*H > best[0]:
                    best = (L*W*H, L, W, H, bricks_needed)

# ---- Final Best Cuboid ----
print("Best Cuboid Dimensions (mm):")
print(f"Length: {best[1]}, Width: {best[2]}, Height: {best[3]}")
print(f"Bricks Used: {best[4]}")
print("\nLocation & Orientation:")
print("• Place cuboid base at origin (0,0,0)")
print("• Length along X-axis, Width along Y-axis, Height along Z-axis")
print("• Bricks aligned such that 200mm side = wall thickness")
