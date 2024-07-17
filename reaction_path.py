import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
from matplotlib.lines import Line2D


def create_stationary_coords(energies, point_width, point_distance):
    points = []
    position = 0.0

    for point in energies:
        points.append((position, point))
        points.append((position + point_width, point))
        position += point_width + point_distance

    return points


def draw_on_plot(
    ax, points, codes, start, length, facecolor, edgecolor, linewidth, linestyle, alpha
):
    for i in range(start, length, 2):
        current_path = Path(points[i : i + 2], codes)
        patch = patches.PathPatch(
            current_path,
            facecolor=facecolor,
            edgecolor=edgecolor,
            linewidth=linewidth,
            linestyle=linestyle,
            alpha=alpha,
        )
        ax.add_patch(patch)


def create_legend_lines(legend_length, point_color):
    lines = []
    for i in range(legend_length):
        lines.append(Line2D([0], [0], color=point_color[i], lw=2))

    return lines


def plot_reaction_profile(
    energies,
    species_labels=None,
    legend_labels=None,
    same_ref=False,
    title=None,
    title_fontweight="normal",
    title_fontsize=10,
    title_color="black",
    figsize=(7, 5),
    save_file=None,
    is_transparent=False,
    image_dpi="figure",
    show_plot=True,
    species_label_offset=0.5,
    species_label_fontweight="normal",
    species_label_fontsize=10,
    species_label_color="black",
    show_energies=False,
    energy_label_offset=0.5,
    energy_label_fontweight="normal",
    energy_label_fontsize=10,
    energy_label_color="black",
    x_margin=0.05,
    y_margin=0.05,
    x_label="Reaction Coordinate",
    x_label_fontweight="normal",
    x_label_fontsize=10,
    x_label_color="black",
    y_label=r"$\Delta$G kcal mol$^{-1}$",
    y_label_fontweight="normal",
    y_label_fontsize=10,
    y_label_color="black",
    y_tick_direction="out",
    y_tick_label_fontsize=10,
    y_tick_label_color="black",
    point_color="black",
    point_alpha=1.0,
    point_width=0.25,
    point_distance=0.5,
    point_linewidth=3,
    point_linestyle="-",
    connector_color="black",
    connector_alpha=0.6,
    connector_linewidth=1,
    connector_linestyle="--",
):

    # Creating xy coordinates for drawing reaction path
    if not isinstance(energies[0], list):
        energies = [energies]
        species_labels = [species_labels]

    pathway_points = []
    for pathway in energies:
        pathway_points.append(
            create_stationary_coords(pathway, point_width, point_distance)
        )

    # Creating figure and axes
    fig, ax = plt.subplots(figsize=figsize)

    # General options how axes and title look
    ax.spines[["right", "top"]].set_visible(False)
    ax.tick_params(axis="x", which="both", bottom=False, labelbottom=False)
    ax.tick_params(
        axis="y",
        which="both",
        direction=y_tick_direction,
        labelsize=y_tick_label_fontsize,
        labelcolor=y_tick_label_color,
    )
    ax.set_xlabel(
        x_label,
        fontweight=x_label_fontweight,
        size=x_label_fontsize,
        color=x_label_color,
    )
    ax.set_ylabel(
        y_label,
        fontweight=y_label_fontweight,
        size=y_label_fontsize,
        color=y_label_color,
    )
    ax.plot(1.0, 0, ">k", transform=ax.transAxes, clip_on=False)
    ax.plot(0, 1.0, "^k", transform=ax.transAxes, clip_on=False)
    ax.margins(x_margin, y_margin)
    ax.set_title(
        title, fontweight=title_fontweight, size=title_fontsize, color=title_color
    )

    # Defining list of codes for drawing stationary pathway_points and connector lines with Path
    codes = [Path.MOVETO, Path.LINETO]

    # Plotting pathway(s)
    for i, pathway in enumerate(pathway_points):
        # Checking if point_colors is string or list
        if not isinstance(point_color, list):
            point_color = [point_color]

        # Draw lines connecting stationary pathway_points
        draw_on_plot(
            ax,
            pathway,
            codes,
            1,
            len(pathway) - 1,
            facecolor="none",
            edgecolor=connector_color,
            linewidth=connector_linewidth,
            linestyle=connector_linestyle,
            alpha=connector_alpha,
        )

        if same_ref and i > 0:
            start = 2
        else:
            start = 0

        # Draw stationary pathway_points
        draw_on_plot(
            ax,
            pathway,
            codes,
            start,
            len(pathway),
            facecolor="none",
            edgecolor=point_color[i],
            linewidth=point_linewidth,
            linestyle=point_linestyle,
            alpha=point_alpha,
        )

    # Adding labels if provided
    if species_labels is not None:
        for i, (pathway_labels, pathway_energies) in enumerate(
            zip(species_labels, energies)
        ):
            current_position = point_width / 2
            for j, (label, energy) in enumerate(zip(pathway_labels, pathway_energies)):

                if i > 0 and j == 0 and same_ref:
                    label = None

                ax.text(
                    current_position,
                    energy + species_label_offset,
                    label,
                    horizontalalignment="center",
                    verticalalignment="bottom",
                    fontweight=species_label_fontweight,
                    size=species_label_fontsize,
                    color=species_label_color,
                )
                current_position = current_position + point_width + point_distance

    # Adding energy labels if provided
    if show_energies:
        for i, pathway_energies in enumerate(energies):
            current_position = point_width / 2
            for j, energy in enumerate(pathway_energies):

                energy_label = energy

                if i > 0 and j == 0 and same_ref:
                    energy_label = None

                ax.text(
                    current_position,
                    energy - energy_label_offset,
                    energy_label,
                    horizontalalignment="center",
                    verticalalignment="top",
                    fontweight=energy_label_fontweight,
                    size=energy_label_fontsize,
                    color=energy_label_color,
                )
                current_position = current_position + point_width + point_distance

    # Adding legend if requested
    if legend_labels is not None:
        lines = create_legend_lines(len(pathway_points), point_color)
        ax.legend(lines, legend_labels)

    if save_file is not None:
        plt.savefig(save_file, transparent=is_transparent, dpi=image_dpi)

    if show_plot:
        plt.show()
