## ReactionPath
A simple Python script to automate the drawing of a reaction profile.

Requires Matplotlib.

### Example Inputs
```
import reaction_path

labels = ["R","TS","P"]
energies = [0.0, 30.0, -20.0]

# Minimal example
reaction_path.plot_reaction_profile(energies)
```

### Example Outputs:
<img src="examples/example1.png" width=60%>

### Options

Many of the below options are just wrappers to common Matplotlib arguments for customising the look of the plot. In theory, any Matplotlib option could be implemented easily.

| Argument                 | Explanation                                                                                                                                         | Default Value                |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| energies                 | List of energies (list of floats)                                                                                                                   | -                            |
| species_labels           | List of labels (list of strings) or list of lists of labels (if multiple pathways requested)                                                        | None                         |
| legend_labels            | List of labels for legend (list of strings)                                                                                                         | None                         |
| same_ref                 | Whether the pathways if multiple have the same reference point (bool)                                                                               | False                        |
| title                    | Title of plot (string)                                                                                                                              | None                         |
| title_fontweight         | Weight of title (Matplotlib valid option)                                                                                                           | "normal"                     |
| title_fontsize           | Fontsize of title (Matplotlib valid option)                                                                                                         | 10                           |
| title_color              | Color of title (Matplotlib valid option)                                                                                                            | "black"                      |
| figsize                  | Size of figure (tuple (width,height) in inches)                                                                                                     | (6,4)                        |
| save_file                | Name of image to be saved (string) - Will not save if None                                                                                          | None                         |
| is_transparent           | Whether to make exported image transparent (bool)                                                                                                   | False                        |
| image_dpi                | DPI of exported image (Matplotlib valid option)                                                                                                     | "figure"                     |
| show_plot                | Whether to show plot (boolean)                                                                                                                      | True                         |
| species_label_offset     | How much to offset species labels from point (float)                                                                                                | 0.5                          |
| species_label_fontweight | Weight of stationary point species label text (Matplotlib valid option)                                                                             | "normal"                     |
| species_label_fontsize   | Fontsize of stationary point species label text (Matplotlib valid option)                                                                           | 10                           |
| species_label_color      | Color of stationary point species label text (Matplotlib valid option)                                                                              | "black"                      |
| energy_label_offset      | How much to offset energy labels from point (float)                                                                                                 | 0.5                          |
| energy_label_fontweight  | Weight of stationary point energy label text (Matplotlib valid option)                                                                              | "normal"                     |
| energy_label_fontsize    | Fontsize of stationary point energy label text (Matplotlib valid option)                                                                            | 10                           |
| energy_label_color       | Color of stationary point energy label text (Matplotlib valid option)                                                                               | "black"                      |
| x_margin                 | How much margin to put on left and right of plot (float)                                                                                            | 0.05                         |
| y_margin                 | How much margin to put on top and bottom of plot (float)                                                                                            | 0.05                         |
| x_label                  | X-axis label (string)                                                                                                                               | "Reaction Coordinate"        |
| x_label_fontweight       | Weight of X-axis label (Matplotlib valid option)                                                                                                    | "normal"                     |
| x_label_fontsize         | Fontsize of X-axis label (Matplotlib valid option)                                                                                                  | 10                           |
| x_label_color            | Color of X-axis label (Matplotlib valid option)                                                                                                     | "black"                      |
| y_label                  | Y-axis label (string)                                                                                                                               | r"$\Delta$G kcal mol$^{-1}$" |
| y_label_fontweight       | Weight of Y-axis label (Matplotlib valid option)                                                                                                    | "normal"                     |
| y_label_fontsize         | Fontsize of Y-axis label (Matplotlib valid option)                                                                                                  | 10                           |
| y_label_color            | Color of Y-axis label (Matplotlib valid option)                                                                                                     | "black"                      |
| y_tick_direction         | Direction of Y-axis tick marks (Matplotlib valid option)                                                                                            | "out"                        |
| y_tick_label_fontsize    | Fontize of Y-axis tick labels (Matplotlib valid option)                                                                                             | 10                           |
| y_tick_label_color       | Color of Y-axis tick labels (Matplotlib valid option)                                                                                               | "black"                      |
| point_color              | Color of stationary point (string or list of Matplotlib colors - if list, will be assigned to multiple pathways based on order of 2D energies list) | "black"                      |
| point_alpha              | Opacity of stationary point (0.0 --> 1.0)                                                                                                           | 1.0                          |
| point_width              | Width of stationary point (float)                                                                                                                   | 0.25                         |
| point_distance           | Distance between stationary points (float)                                                                                                          | 0.5                          |
| point_linewidth          | Linewidth of stationary point (float)                                                                                                               | 3                            |
| point_linestyle          | Linestyle of stationary point (Matplotlib valid option)                                                                                             | 3                            |
| connector_color          | Color of connector lines (Matplotlib valid color)                                                                                                   | "black"                      |
| connector_alpha          | Opacity of connector lines (0.0 --> 1.0)                                                                                                            | 0.6                          |
| connector_linewidth      | Linewidth of connector lines (float)                                                                                                                | 1                            |
| connector_linestyle      | Linestyle of connector lines (Matplotlib valid linestyle)                                                                                           | "--"                         |
