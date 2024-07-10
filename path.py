import matplotlib.pyplot as plt
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

print(points)
