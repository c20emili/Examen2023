import statsmodels.stats.multicomp as multi
import pandas as pd
import matplotlib.pyplot as plt

def tuckeyTest(*data, groups):

    # Put data into dataframe
    df = pd.DataFrame()

    if len(data) == 2:
        print ("Tuckey test requires more than two data sources")
    elif len(data) == 3:
        df[ groups[0] ] = data[0]
        df[ groups[1] ] = data[1]
        df[ groups[2] ] = data[2]
    elif len(data) == 4:
        df[ groups[0] ] = data[0]
        df[ groups[1] ] = data[1]
        df[ groups[2] ] = data[2]
        df[ groups[3] ] = data[3]
    elif len(data) == 5:
        df[ groups[0] ] = data[0]
        df[ groups[1] ] = data[1]
        df[ groups[2] ] = data[2]
        df[ groups[3] ] = data[3]
        df[ groups[4] ] = data[4]
    elif len(data) == 6:
        df[ groups[0] ] = data[0]
        df[ groups[1] ] = data[1]
        df[ groups[2] ] = data[2]
        df[ groups[3] ] = data[3]
        df[ groups[4] ] = data[4]
        df[ groups[5] ] = data[5]


    # Stack the data (and rename columns):
    stacked_data = df.stack().reset_index()
    stacked_data = stacked_data.rename(columns={'level_0': 'id', 'level_1': 'treatment', 0:'result'})

    # Show the stacked data:
    # print (stacked_data)

    # Show all pair-wise comparisons:

    res2 = multi.pairwise_tukeyhsd (stacked_data['result'], stacked_data['treatment'])
    print(res2)

    # plot Simultaneous Confidence Intervals
    res2.plot_simultaneous()

    # if you want to scompute and show the Grand Mean line
    grandMean = stacked_data['result'].values.mean()
    #plt.vlines(x=grandMean, ymin=-0.5, ymax=4.5, color="red")
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.title('Multiple Comparison between all pairs (Tukey)', fontsize=15)

    plt.savefig("Tukey.png", bbox_inches='tight')


# Prepare data for Tuckey test


#Read your data from file
df = pd.read_csv('mergedAll.csv', keep_default_na=False, sep=",", header=None, names=['nr', 'TetrahedronB', 'OctahedronB', 'IcosahedronB', 'TetrahedronA', 'OctahedronA', 'IcosahedronA'])


tuckeyTest(df['TetrahedronB'], df['OctahedronB'], df['IcosahedronB'],df['TetrahedronA'], df['OctahedronA'], df['IcosahedronA'], groups=['Tetrahedron Babylon', 'Octahedron Babylon', 'Icosahedron Babylon', 'Tetrahedron A-Frame', 'Octahedron A-Frame', 'Icosahedron A-Frame'])
