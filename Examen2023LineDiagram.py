import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure

figure(figsize=(10, 5))
#figure(figsize=(18, 5))


# import glob
# Read your data from file
df1 = pd.read_csv('TestDataBabylon.csv', keep_default_na=False, sep=",", header=None, names=['nr', 'Frames', 'empty'])
df2 = pd.read_csv('TestDataA-Frame.csv', keep_default_na=False, sep=",", header=None, names=['nr', 'Frames', 'empty'])

# dfB = pd.read_csv('mergedB.csv', keep_default_na=False, sep=",", header=None, names=['nr', 'TetrahedronB', 'OctahedronB', 'IcosahedronB'])
# dfA = pd.read_csv('mergedA.csv', keep_default_na=False, sep=",", header=None, names=['nr', 'TetrahedronA', 'OctahedronA', 'IcosahedronA'])
df = pd.read_csv('mergedAll.csv', keep_default_na=False, sep=",", header=None, names=['nr', 'TetrahedronB', 'OctahedronB', 'IcosahedronB', 'TetrahedronA', 'OctahedronA', 'IcosahedronA'])

# Plot line serie of data
x = range(0, len(df1['nr'].tolist()))
# df['word'].tolist() #because the following plot takes list of data
y1 = df1['Frames'].tolist()  # because the following plot takes list of data
y2 = df2['Frames'].tolist()  # because the following plot takes list of data
yB1 = df['TetrahedronB'].tolist()  # because the following plot takes list of data
yB2 = df['OctahedronB'].tolist()  # because the following plot takes list of data
yB3 = df['IcosahedronB'].tolist()  # because the following plot takes list of data
yA1 = df['TetrahedronA'].tolist()  # because the following plot takes list of data
yA2 = df['OctahedronA'].tolist()  # because the following plot takes list of data
yA3 = df['IcosahedronA'].tolist()  # because the following plot takes list of data
# transparency of lines
a = 0.75;
#figure(figsize=(10, 5), dpi=100)
#plt.plot(x, y1, color='red', label="Babylon.js", alpha=a, linewidth=0.7)
plt.plot(x, y2, color='green', label="A-Frame", alpha=a, linewidth=0.7)
#plt.plot(x, yB1, color='red', label="Tetrahedron(4) Babylon.js", alpha=a, linewidth=0.7)
#plt.plot(x, yB2, color='cyan', label="Octahedron(8) Babylon.js", alpha=a, linewidth=0.7)
#plt.plot(x, yB3, color='blue', label="Icosahedron(20) Babylon.js", alpha=a, linewidth=0.7)
#plt.plot(x, yA1, color='green', label="Tetrahedron(4) A-Frame", alpha=a, linewidth=0.7)
#plt.plot(x, yA2, color='purple', label="Octahedron(8) A-Frame", alpha=a, linewidth=0.7)
#plt.plot(x, yA3, color='orange', label="Icosahedron(20) A-Frame", alpha=a, linewidth=0.7)
leg = plt.legend(fontsize=15)
# set the linewidth of each legend object
for legobj in leg.legend_handles:
    legobj.set_linewidth(2.0)
plt.yticks(np.arange(0, 70, 5), fontsize=15)
#plt.xticks(np.arange(0, 6000, 500), fontsize=15)
plt.xticks(np.arange(0, 650, 50), fontsize=15)
plt.ylim(0, 65)
#plt.xlim(0,5000)
plt.xlim(0,600)
plt.xlabel('Time', fontsize=20)
plt.ylabel('Frames', fontsize=20)
plt.title('Frames per second \n A-Frame', fontsize=25)
plt.grid(True)
plt.savefig('lineDiagramA.png', bbox_inches='tight')
#plt.show()
