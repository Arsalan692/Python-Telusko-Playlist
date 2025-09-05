import matplotlib.pyplot as mp
import numpy as np

# The number of arguments in one array should be equal to the argument of another array
x = np.array([0,12,34,44,52,55,60,80,91, 100])
y = np.array([2, 5, 8, 9, 10,12,14,16,18,20])

# The first argument is the x-axis and the other is y-axis!
# The third argument is use to scatter data according to the string.
# mp.plot(x,y,"o")

# This command add lines like plot graph on the graph
# mp.grid()

# This command is use to show the graph on the screen
# mp.show()

# # Matplotlib's default x-axis and y-axis
# mp.plot(x)
# mp.show()

# Markers in Matplotlib
# mp.plot(x,y,marker="*")
# mp.show()

# Colors in matplotlib
# marker --> To choose the style of the marker
# color --> To choose the color of the graph line
# linestyle --> To choose the style of the graph line
# markersize --> To choose the size of the marker
# markerfacecolor --> To choose the color of the marker
# markeredgecolor --> To choose the marker edge(boundary) color
mp.plot(x, y,
        marker="o",
        color="blue",
        linestyle="-.",
        markersize=6,
        markerfacecolor="red",
        markeredgecolor="black",
        linewidth=2)
mp.grid()
mp.show()
















