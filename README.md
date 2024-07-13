## ReactionPath
A simple Python script to automate the drawing of a reaction profile.

Requires Matplotlib.

### Example Inputs
```
import path

labels = ["R","I1","TS1","I2","TS2","I3","TS3","P"]
energies = [0.0, 5.0, 30.0, -20.0, 10.0, -30.0, 5.0, -40.0]

path.plot_reaction_profile(energies, labels=labels, title="Example 1")
path.plot_reaction_profile(energies, labels=labels, label_fontweight="bold", title="Example 2", point_color="red",
                           point_width=2.0, point_distance=1.0, connector_linestyle="-", connector_alpha=1.0)

```

### Example Outputs:
![Example 1](examples/example1.png)

![Example 2](examples/example2.png)

### Options


| Argument            | Explanation                                                       | Default Value                |
|---------------------|-------------------------------------------------------------------|------------------------------|
| energies            | List of energies (list of floats)                                 | -                            |
| labels              | List of labels (list of strings)                                  | None                         |
| title               | Title of plot (string)                                            | None                         |
| figsize             | Size of figure (tuple (width,height) in inches)                   | (8,6)                        |
| save_file           | Name of image to be saved (string) - Will not save if None        | None                         |
| show_plot           | Whether to show plot (boolean)                                    | True                         |
| label_offset        | How much to offset labels from point (float)                      | 0.5                          |
| label_fontweight    | Weight of stationary point label text (Matplotlib valid option)   | "normal"                     |
| label_fontsize      | Fontsize of stationary point label text (Matplotlib valid option) | 10                           |
| x_margin            | How much margin to put on left and right of plot (float)          | 0.05                         |
| y_margin            | How much margin to put on top and bottom of plot (float)          | 0.05                         |
| x_label             | X-axis label (string)                                             | "Reaction Coordinate"        |
| x_label_fontweight  | Weight of X-axis label (Matplotlib valid option)                  | "normal"                     |
| x_label_fontsize    | Fontsize of X-axis label (Matplotlib valid option)                | 10                           |
| x_label_color       | Color of X-axis label (Matplotlib valid option)                   | "black"                      |
| y_label             | Y-axis label (string)                                             | r"$\Delta$G kcal mol$^{-1}$" |
| y_label_fontweight  | Weight of Y-axis label (Matplotlib valid option)                  | "normal"                     |
| y_label_fontsize    | Fontsize of Y-axis label (Matplotlib valid option)                | 10                           |
| y_label_color       | Color of Y-axis label (Matplotlib valid option)                   | "black"                      |
| point_color         | Color of stationary point (any Matplotlib color)                  | "black"                      |
| point_alpha         | Opacity of stationary point (0.0 --> 1.0)                         | 1.0                          |
| point_width         | Width of stationary point (float)                                 | 0.25                         |
| point_distance      | Distance between stationary points (float)                        | 0.5                          |
| point_linewidth     | Linewidth of stationary point (float)                             | 3                            |
| connector_color     | Color of connector lines (Matplotlib valid color)                 | "black"                      |
| connector_alpha     | Opacity of connector lines (0.0 --> 1.0)                          | 0.6                          |
| connector_linewidth | Linewidth of connector lines (float)                              | 1                            |
| connector_linestyle | Linestyle of connector lines (Matplotlib valid linestyle)         | "--"                         |
