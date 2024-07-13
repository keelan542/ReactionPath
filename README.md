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
```
def plot_reaction_profile(energies, labels=None, title=None, figsize=(8,6),
                          label_offset=0.5, label_fontweight="normal", x_margin=0.05, y_margin=0.05,
                          x_label="Reaction Coordinate", y_label=r"$\Delta$G kcal mol$^{-1}$", point_color="black", point_alpha=1.0,
                          point_width=0.25, point_distance=0.5, point_linewidth=3, connector_color="black",
                          connector_alpha=0.6, connector_linewidth=1, connector_linestyle="--"):
```

| Argument            | Explanation                                                     |
|---------------------|-----------------------------------------------------------------|
| energies            | List of energies (list of floats)                               |
| labels              | List of labels (list of strings)                                |
| title               | Title of plot (string)                                          |
| figsize             | Size of figure (tuple (width,height) in inches)                 |
| label_offset        | How much to offset labels from point (float)                    |
| label_fontweight    | Weight of stationary point label text (Matplotlib valid option) |
| x_margin            | How much margin to put on left and right of plot (float)        |
| y_margin            | How much margin to put on top and bottom of plot (float)        |
| x_label             | X-axis label (string)                                           |
| y_label             | Y-axis label (string)                                           |
| point_color         | Color of stationary point (any Matplotlib color)                |
| point_alpha         | Opacity of stationary point (0.0 --> 1.0)                       |
| point_width         | Width of stationary point (float)                               |
| point_distance      | Distance between stationary points (float)                      |
| point_linewidth     | Linewidth of stationary point (float)                           |
| connector_color     | Color of connector lines (Matplotlib valid color)               |
| connector_alpha     | Opacity of connector lines (0.0 --> 1.0)                        |
| connector_linewidth | Linewidth of connector lines (float)                            |
| connector_linestyle | Linestyle of connector lines (Matplotlib valid linestyle)       |
