Simple Python script to automate the drawing of a reacion profile.

Usage:
```
import path

labels = ["R","I1","TS1","I2","TS2","I3","TS3","I4","P"]
energies = [0.0, 5.0, 30.0, -20.0, 10.0, -30.0, 5.0, -40.0]

path.plot_reaction_profile(energies=energies, labels=labels)

```

Example Output:
![Example Plot](example_plot.png)

Requires Matplotlib.