import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from matplotlib.transforms import Affine2D
import numpy as np
import scipy.stats as stats

figure(figsize=(10, 5), dpi=80)
def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), stats.sem(a)
    h = se * stats.t.ppf((1 + confidence) / 2., n-1)
    return -h, +h

def exampleBarChars():
    # Read your data from file
    df = pd.read_csv('mergedFrames.csv', sep=",", header=None, names=['nr', 'Babylon', 'A-Frame'])

    # width of the bars
    barWidth = 0.6
    print(df['Babylon'].mean())
    print(df['A-Frame'].mean())
    # Bars Data
    barsData = [df['Babylon'].mean(), df['A-Frame'].mean()]

    # The x-position order of bars
    barsOrder = range(len([df['Babylon'], df['A-Frame']]))

    # Std Bars Interval
    barsInterval = [df['Babylon'].std(), df['A-Frame'].std()]

    # Standard Error Bars intervals
    barsInterval2 = [df['Babylon'].sem(), df['A-Frame'].sem()]



    CI_Base = mean_confidence_interval(df['Babylon'])
    CI_Cache = mean_confidence_interval(df['A-Frame'])
    df_CI = pd.DataFrame(list(zip(CI_Base, CI_Cache)), columns=['Babylon', 'A-Frame'])
    barsInterval3 = df_CI.iloc[1]

    # Colours of bar charts
    colors = ["red", "green"]

    # Opacity of colours
    Opacity = 0.5

    # Start values from bottom of the bars
    minValue = [df['Babylon'].values.min(), df['A-Frame'].values.min()]
    test = min(minValue)

    # Interval cap size
    intervalCapsize = 7


    # Plot bars
    plt.bar(barsOrder, barsData, color=colors, edgecolor='black', width=barWidth, yerr=barsInterval3, ecolor="black", capsize=5, alpha=Opacity, bottom=0)

    # Put a tick on the x-axis undex each bar and label it with column name
    plt.xticks(range(2), ['Babylon', 'A-Frame'])

    plt.ylabel('Frames')
    plt.ylim(55, 65)
    plt.title('Frames per second with \n Confidence interval')
    #plt.show()
    plt.savefig('FramesCI.png')


exampleBarChars()
