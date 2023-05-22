import pandas as pd

# reading csv files
dfB1 = pd.read_csv('B1.csv', keep_default_na=False, sep=",", header=None, names=['nr', 'TetrahedronB'])
dfB2 = pd.read_csv('B2.csv', keep_default_na=False, sep=",", header=None, names=['nr', 'OctahedronB'])
dfB3 = pd.read_csv('B3.csv', keep_default_na=False, sep=",", header=None, names=['nr', 'IcosahedronB'])
dfA1 = pd.read_csv('A1.csv', keep_default_na=False, sep=",", header=None, names=['nr', 'TetrahedronA'])
dfA2 = pd.read_csv('A2.csv', keep_default_na=False, sep=",", header=None, names=['nr', 'OctahedronA'])
dfA3 = pd.read_csv('A3.csv', keep_default_na=False, sep=",", header=None, names=['nr', 'IcosahedronA'])

# using merge function by setting how='inner'
output1 = pd.merge(dfB1, dfB2, on=['nr'], how='inner')
output2 = pd.merge(dfB1, dfB3, on=['nr'], how='inner')
output3 = pd.merge(output1, output2, on=['nr','TetrahedronB'], how='inner')
output3.to_csv('mergedB.csv')
output4 = pd.merge(dfA1, dfA2, on=['nr'], how='inner')
output5 = pd.merge(dfA1, dfA3, on=['nr'], how='inner')
output6 = pd.merge(output4, output5, on=['nr','TetrahedronA'], how='inner')
output6.to_csv('mergedA.csv')
output7 = pd.merge(output3, output6, on=['nr'], how='inner')
output7.to_csv('mergedAll.csv')
# displaying result
print(output7)
