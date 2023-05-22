import scipy.stats as stats
import numpy as np
import statsmodels.stats.multicomp as multi
import pandas as pd


def anova(*data): # * indicates, 0, 1 , 2 .. arguments

    if len(data) == 2:
        statistic, pvalue = stats.f_oneway(data[0], data[1])
    elif len(data) == 3:
        statistic, pvalue = stats.f_oneway(data[0], data[1], data[2])
    elif len(data) == 4:
        statistic, pvalue = stats.f_oneway(data[0], data[1], data[2], data[3])


    print("ANOVA Statistic " + str(statistic) + " and p-value " + str(pvalue))

    if pvalue < 0.05: #alpha = 0.05
        return True
    else:
        return False



def exampleAnova():

    #Read your data from file
    #df = pd.read_csv('mergedFrames.csv', sep=",", header=None, names=['nr', 'Babylon', 'A-Frame'])
    df = pd.read_csv('mergedAll.csv', keep_default_na=False, sep=",", header=None, names=['nr', 'TetrahedronB', 'OctahedronB', 'IcosahedronB', 'TetrahedronA', 'OctahedronA', 'IcosahedronA'])

    #Run Anova on data groups
    if (anova (df['TetrahedronB'], df['TetrahedronA'])):
        print ("The means are different")
    else:
        print ("No differences in means")

exampleAnova()
