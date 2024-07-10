import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

# Dictionaries storing pathways
test_path = {"R" : 0.0, "I1": 5.0, "TS1" : 30.0, "P" : -20.0}

# Creating xy coordinates for drawing reaction path
points = []
position = 0.0
for point in test_path:
    points.append((position, test_path[point]))
    points.append((position+0.25, test_path[point]))
    position += 0.5

# Creating figure and axes
fig, ax = plt.subplots()

# Defining limits of plot
min_energy = min(test_path.values())
max_energy = max(test_path.values())
ax.set_xlim(-1, 2)
ax.set_ylim(min_energy - 5.0, max_energy + 5.0)

# Some aesthetic stuff
ax.spines[['right', 'top']].set_visible(False)
ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
ax.set_xlabel("Reaction Coordinate")
ax.set_ylabel(r"G kcal / mole$^{-1}$")
ax.plot(1.0, 0, '>k', transform=ax.transAxes, clip_on=False)

# Draw dashed connector lines first
codes = [Path.MOVETO]
codes.extend([Path.LINETO] * (len(points)-1))
dashed_path = Path(points, codes)
patch = patches.PathPatch(dashed_path, facecolor="none", lw=1, linestyle="--")
ax.add_patch(patch)

# Draw stationary point bolded lines next
codes = [Path.MOVETO, Path.LINETO]
for i in range(0, len(points), 2):
    path = Path(points[i:i+2], codes)
    patch = patches.PathPatch(path, facecolor="none", lw=3)
    ax.add_patch(patch)

plt.show()
