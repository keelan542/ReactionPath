import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

def plot_reaction_profile(energies, labels=None, point_width=0.25, point_distance=0.5, start = 0.5):
    # Creating xy coordinates for drawing reaction path
    points = []
    position = start
    for point in energies:
        points.append((position, point))
        points.append((position + point_width, point))
        position += (point_width + point_distance)

    # Creating figure and axes
    fig, ax = plt.subplots()

    # Some aesthetic stuff
    ax.spines[['right', 'top']].set_visible(False)
    ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    ax.set_xlabel("Reaction Coordinate")
    ax.set_ylabel(r"$\Delta$G kcal mole$^{-1}$")
    ax.plot(1.0, 0, '>k', transform=ax.transAxes, clip_on=False)
    ax.plot(0, 1.0, '^k', transform=ax.transAxes, clip_on=False)

    # Draw dashed connector lines first
    codes = [Path.MOVETO]
    codes.extend([Path.LINETO] * (len(points)-1))
    dashed_path = Path(points, codes)
    patch = patches.PathPatch(dashed_path, facecolor="none", lw=1, linestyle="--", alpha=0.6)
    ax.add_patch(patch)

    # Draw stationary point bolded lines next
    codes = [Path.MOVETO, Path.LINETO]
    for i in range(0, len(points), 2):
        path = Path(points[i:i+2], codes)
        patch = patches.PathPatch(path, facecolor="none", lw=3)
        ax.add_patch(patch)

    # Adding labels to points if provided
    if labels is not None:
        current_position = start + (point_width / 2)
        print(current_position)
        for label, energy in zip(labels, energies):
            ax.text(current_position, energy, label, horizontalalignment="center", verticalalignment="bottom")
            current_position = current_position + point_width + point_distance
            print(current_position)

    plt.show()