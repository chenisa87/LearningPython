import matplotlib.pyplot as plt

# Set up the figure and subplot
fig, ax = plt.subplots()

# Draw the head and ears
ax.plot([1, 1], [1, 2], 'b', linewidth=2)
ax.plot([2, 3], [2, 3], 'b', linewidth=2)
ax.plot([3, 3], [1, 2], 'b', linewidth=2)

# Draw the eyes
ax.plot([1.5, 1.5], [1.5, 1.7], 'g', linewidth=2)
ax.plot([2.5, 2.5], [1.5, 1.7], 'g', linewidth=2)

# Draw the nose and mouth
ax.plot([2, 2], [1.5, 1.2], 'r', linewidth=2)
ax.plot([1.5, 2.5], [1.2, 1.2], 'r', linewidth=2)

# Set the x and y limits
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)

# Show the plot
plt.show()