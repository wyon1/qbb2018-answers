#!/usr/bin/env python3

"""


./clustering.py <hema_data.txt>
"""

import sys
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
import numpy as np
import seaborn as sns


file = open(sys.argv[1])

header = file.readline()
celltype = header.split()
celltype_label = celltype[1:]
genes = []
data = []
for line in file:
   fields = line.split()
   genes.append(fields[0])
   data_row = []
   for fpkm in fields[1:]:
       data_row.append(float(fpkm))
   data.append(data_row)

X = np.array(data)
genes = np.array(genes)

Z = linkage(X, method='average', metric='euclidean', optimal_ordering=True)
gene_index = leaves_list(Z)

Z_T = linkage(X.T, method='average', metric='euclidean', optimal_ordering=True)
cell_index = leaves_list(Z_T)

plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(
    Z,
    leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
)
plt.savefig('dendrogram')


labels = np.array(celltype_label)
species = genes

sorted_X = X[gene_index]
sorted_X = sorted_X[:, cell_index]

# Make the actual plot
fig, ax = plt.subplots(figsize=(8, 6))          # Open a blank canvas, 8 inches x 6 inches
ax.set_title("Heatmap of things") # Add a title to the top
im = ax.pcolor(                              # Treat the values like pixel intensities in a picture
	sorted_X,                                       # ... Using X as the values
	cmap="RdBu",                             # ... Use the Red-white-blue colormap to assign colors to your pixel values
#	vmin=-1                               # ... Set the lowest value to show on the scale
#	vmax=m,                                  # ... Set the highest value to show on the scale. Since we are using a 'diverging' colormap, these should match.
	)

ax.grid(False)                      # Turn of the grid lines (a feature added automatically by ggplot)
ax.set_xticks(                      # Edit the xticks being shown
	np.arange(0.5, X.shape[1]+0.5), # ... use the values centered on each column of pixels
	)
ax.set_xticklabels(                 # Label the ticks
	labels[cell_index],                         # ... at position which correspond to the indices of our labels
	rotation=50,                    # ... and rotate the labels 50 degrees counter-clockwise
	)
ax.set_yticks([])                   # Edit the ticks on the y-axis to show....NOTHING

cbar = fig.colorbar(im, ax=ax)      # Add a bar to the right side of the plot which shows the scale correlating the colors to the pixel values

fig.subplots_adjust( # Adjust the spacing of the subplots, to help make everything fit
    left = 0.05,     # ... the left edge of the left-most plot will be this percent of the way across the width of the plot
    bottom = 0.15,   # ... the bottom edge of the bottom-most plot will be this percent of the way up the canvas
    right = 1.0,     # ... the right edge of the right-most plot will be this percent of the way across the width
    top = 0.95,      # ... the top edge of the top-most plot will be this percent of the way from the bottom
)

fig.savefig("clean_heatmap.png") # Save the image
plt.close(fig) # Close the canvas
