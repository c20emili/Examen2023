import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from matplotlib.transforms import Affine2D
import numpy as np
import scipy.stats as stats

figure(figsize=(10, 5))
#figure(figsize=(18, 5))
def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), stats.sem(a)
    h = se * stats.t.ppf((1 + confidence) / 2., n-1)
    return -h, +h

def exampleBarChars():
    # Read your data from file
    df = pd.read_csv('mergedAll.csv', keep_default_na=False, sep=",", header=None, names=['nr', 'TetrahedronB', 'OctahedronB', 'IcosahedronB', 'TetrahedronA', 'OctahedronA', 'IcosahedronA'])
    df1 = pd.read_csv('TestDataBabylon.csv', keep_default_na=False, sep=",", header=None, names=['nr', 'Frames', 'empty'])
    df2 = pd.read_csv('TestDataA-Frame.csv', keep_default_na=False, sep=",", header=None, names=['nr', 'Frames', 'empty'])

    # width of the bars
    barWidth = 0.6
    print(df['TetrahedronB'].mean())
    print(df['OctahedronB'].mean())
    print(df['IcosahedronB'].mean())
    print(df['TetrahedronA'].mean())
    print(df['OctahedronA'].mean())
    print(df['IcosahedronA'].mean())

    # Bars Data
    testbarsData = [df1['Frames'].mean(), df2['Frames'].mean()]
    barsData = [df['TetrahedronB'].mean(), df['OctahedronB'].mean(), df['IcosahedronB'].mean(), df['TetrahedronA'].mean(), df['OctahedronA'].mean(), df['IcosahedronA'].mean()]
    barsDataB = [df['TetrahedronB'].mean(), df['OctahedronB'].mean(), df['IcosahedronB'].mean()]
    barsDataA = [df['TetrahedronA'].mean(), df['OctahedronA'].mean(), df['IcosahedronA'].mean()]
    barsDataT = [df['TetrahedronB'].mean(), df['TetrahedronA'].mean()]
    barsDataO = [df['OctahedronB'].mean(), df['OctahedronA'].mean()]
    barsDataI = [df['IcosahedronB'].mean(), df['IcosahedronA'].mean()]

    # Number of columns
    amount1 = 6
    amount2 = 3
    amount3 = 2

    # The x-position order of bars
    barsOrder = range(len([df['TetrahedronB'], df['OctahedronB'], df['IcosahedronB'], df['TetrahedronA'], df['OctahedronA'], df['IcosahedronA']]))
    barsOrder1 = range(amount1)
    barsOrder2 = range(amount2)
    barsOrder3 = range(amount3)

    # Std Bars Interval
    testbarsInterval = [df1['Frames'].std(), df2['Frames'].std()]
    barsInterval = [df['TetrahedronB'].std(), df['OctahedronB'].std(), df['IcosahedronB'].std(), df['TetrahedronA'].std(), df['OctahedronA'].std(), df['IcosahedronA'].std()]
    barsIntervalB = [df['TetrahedronB'].std(), df['OctahedronB'].std(), df['IcosahedronB'].std()]
    barsIntervalA = [df['TetrahedronA'].std(), df['OctahedronA'].std(), df['IcosahedronA'].std()]
    barsIntervalT = [df['TetrahedronB'].std(), df['TetrahedronA'].std()]
    barsIntervalO = [df['OctahedronB'].std(), df['OctahedronA'].std()]
    barsIntervalI = [df['IcosahedronB'].std(), df['IcosahedronA'].std()]

    # Standard Error Bars intervals
    testbarsInterval2 = [df1['Frames'].sem(), df2['Frames'].sem()]
    barsInterval2 = [df['TetrahedronB'].sem(), df['OctahedronB'].sem(), df['IcosahedronB'].sem(), df['TetrahedronA'].sem(), df['OctahedronA'].sem(), df['IcosahedronA'].sem()]
    barsIntervalB2 = [df['TetrahedronB'].sem(), df['OctahedronB'].sem(), df['IcosahedronB'].sem()]
    barsIntervalA2 = [df['TetrahedronA'].sem(), df['OctahedronA'].sem(), df['IcosahedronA'].sem()]
    barsIntervalT2 = [df['TetrahedronB'].sem(), df['TetrahedronA'].sem()]
    barsIntervalO2 = [df['OctahedronB'].sem(), df['OctahedronA'].sem()]
    barsIntervalI2 = [df['IcosahedronB'].sem(), df['IcosahedronA'].sem()]

    CI_B1 = mean_confidence_interval(df['TetrahedronB'])
    CI_B2 = mean_confidence_interval(df['OctahedronB'])
    CI_B3 = mean_confidence_interval(df['IcosahedronB'])
    CI_A1 = mean_confidence_interval(df['TetrahedronA'])
    CI_A2 = mean_confidence_interval(df['OctahedronA'])
    CI_A3 = mean_confidence_interval(df['IcosahedronA'])
    TCI_A = mean_confidence_interval(df2['Frames'])
    TCI_B = mean_confidence_interval(df1['Frames'])

    df_CI = pd.DataFrame(list(zip(CI_B1, CI_B2, CI_B3, CI_A1, CI_A2, CI_A3)), columns=['TetrahedronB', 'OctahedronB', 'IcosahedronB', 'TetrahedronA', 'OctahedronA', 'IcosahedronA'])
    dfB_CI = pd.DataFrame(list(zip(CI_B1, CI_B2, CI_B3)), columns=['TetrahedronB', 'OctahedronB', 'IcosahedronB'])
    dfA_CI = pd.DataFrame(list(zip(CI_A1, CI_A2, CI_A3)), columns=['TetrahedronA', 'OctahedronA', 'IcosahedronA'])
    dfT_CI = pd.DataFrame(list(zip(CI_B1, CI_A1)), columns=['TetrahedronB', 'TetrahedronA'])
    dfO_CI = pd.DataFrame(list(zip(CI_B2, CI_A2)), columns=['OctahedronB', 'OctahedronA'])
    dfI_CI = pd.DataFrame(list(zip(CI_B3, CI_A3)), columns=['IcosahedronB', 'IcosahedronA'])
    Tdf_CI = pd.DataFrame(list(zip(TCI_B, TCI_A)), columns=['Babylon.js', 'A-Frame'])

    testbarsInterval3 = Tdf_CI.iloc[1]
    barsInterval3 = df_CI.iloc[1]
    barsIntervalB3 = dfB_CI.iloc[1]
    barsIntervalA3 = dfA_CI.iloc[1]
    barsIntervalT3 = dfT_CI.iloc[1]
    barsIntervalO3 = dfO_CI.iloc[1]
    barsIntervalI3 = dfI_CI.iloc[1]

    # Colours of bar charts
    colors = ["red", "cyan", "blue", "green", "purple", "orange"]
    colorsB = ["red", "yellow", "blue"]
    colorsA = ["green", "purple", "orange"]
    colorsT = ["red", "green"]
    colorsO = ["yellow", "purple"]
    colorsI = ["blue", "orange"]


    # Opacity of colours
    Opacity = 0.5

    # Start values from bottom of the bars
    # minValue = [df['Tetrahedron(4)'].values.min(), df['Octahedron(8)'].values.min(), df['Icosahedron(20)'].values.min()]
    # test = min(minValue)

    # Columns
    columns = ['Tetrahedron(4) \n Babylon', 'Octahedron(8) \n Babylon', 'Icosahedron(20) \n Babylon', 'Tetrahedron(4) \n A-Frame', 'Octahedron(8) \n A-Frame', 'Icosahedron(20) \n A-Frame']
    columnsB = ['Tetrahedron(4) Babylon', 'Octahedron(8) Babylon', 'Icosahedron(20) Babylon']
    columnsA = ['Tetrahedron(4) A-Frame', 'Octahedron(8) A-Frame', 'Icosahedron(20) A-Frame']
    columnsT = ['Tetrahedron(4) Babylon', 'Tetrahedron(4) A-Frame']
    columnsO = ['Octahedron(8) Babylon', 'Octahedron(8) A-Frame']
    columnsI = ['Icosahedron(20) Babylon', 'Icosahedron(20) A-Frame']
    testcolumns = ['Babylon.js', 'A-Frame']

    # Plot bars
    plt.bar(barsOrder3, testbarsData, color=colorsT, edgecolor='black', width=barWidth, yerr=testbarsInterval, ecolor="black", capsize=5, alpha=Opacity, bottom=0)

    # Put a tick on the x-axis undex each bar and label it with column name
    plt.xticks(range(amount3), testcolumns, fontsize=15)

    plt.ylabel('Frames', fontsize=20)
    plt.yticks(np.arange(0, 70, 5), fontsize=15)
    plt.ylim(0, 65)
    plt.title('Frames per second with standard deviation', fontsize=25)
    #plt.show()
    plt.savefig('testStd.png', bbox_inches='tight')


exampleBarChars()
