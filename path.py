import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path

def plot_reaction_profile(energies, labels=None, title=None, title_fontweight="normal", title_fontsize=10,
                          title_color="black", figsize=(7,5), save_file=None, show_plot=True,
                          label_offset=0.5, label_fontweight="normal", label_fontsize=10, label_color="black", x_margin=0.05,
                          y_margin=0.05, x_label="Reaction Coordinate", x_label_fontweight="normal", x_label_fontsize=10, x_label_color="black",
                          y_label=r"$\Delta$G kcal mol$^{-1}$", y_label_fontweight="normal", y_label_fontsize=10, y_label_color="black",
                          x_tick_direction="out", x_tick_label_fontsize=10, x_tick_label_color="black", point_color="black",
                          point_alpha=1.0, point_width=0.25, point_distance=0.5, point_linewidth=3,
                          connector_color="black", connector_alpha=0.6, connector_linewidth=1, connector_linestyle="--"):

    # Creating xy coordinates for drawing reaction path
    points = []
    position = 0.0
    for point in energies:
        points.append((position, point))
        points.append((position + point_width, point))
        position += (point_width + point_distance)

    # Creating figure and axes
    fig, ax = plt.subplots(figsize=figsize)

    # Some aesthetic stuff
    ax.spines[['right', 'top']].set_visible(False)
    ax.tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    ax.tick_params(axis='y', which='both', direction=x_tick_direction, labelsize=x_tick_label_fontsize, labelcolor=x_tick_label_color)
    ax.set_xlabel(x_label, fontweight=x_label_fontweight, size=x_label_fontsize, color=x_label_color)
    ax.set_ylabel(y_label, fontweight=y_label_fontweight, size=y_label_fontsize, color=y_label_color)
    ax.plot(1.0, 0, '>k', transform=ax.transAxes, clip_on=False)
    ax.plot(0, 1.0, '^k', transform=ax.transAxes, clip_on=False)
    ax.margins(x_margin, y_margin)
    ax.set_title(title, fontweight=title_fontweight, size=title_fontsize, color=title_color)

    # Draw dashed connector lines first
    codes = [Path.MOVETO]
    codes.extend([Path.LINETO] * (len(points)-1))
    dashed_path = Path(points, codes)
    patch = patches.PathPatch(dashed_path, facecolor="none", edgecolor=connector_color, linewidth=connector_linewidth,
                              linestyle=connector_linestyle, alpha=connector_alpha)
    ax.add_patch(patch)

    # Draw stationary point bolded lines next
    codes = [Path.MOVETO, Path.LINETO]
    for i in range(0, len(points), 2):
        path = Path(points[i:i+2], codes)
        patch = patches.PathPatch(path, facecolor="none", edgecolor=point_color, linewidth=point_linewidth, alpha=point_alpha)
        ax.add_patch(patch)

    # Adding labels to points if provided
    if labels is not None:
        current_position = (point_width / 2)
        for label, energy in zip(labels, energies):
            ax.text(current_position, energy + label_offset, label, horizontalalignment="center",
                    verticalalignment="bottom", fontweight=label_fontweight, size=label_fontsize, color=label_color)
            current_position = current_position + point_width + point_distance

    if save_file is not None:
        plt.savefig(save_file)

    if show_plot:
        plt.show()