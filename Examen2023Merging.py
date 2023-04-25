import pandas as pd

# reading two csv files
df1 = pd.read_csv('TestDataBabylon2.csv', keep_default_na=False, sep=",", header=None, names=['nr', 'Babylon'])
df2 = pd.read_csv('TestDataA-Frame2.csv', keep_default_na=False, sep=",", header=None, names=['nr', 'A-Frame'])

# using merge function by setting how='inner'
output1 = pd.merge(df1, df2, on=['nr'], how='inner')
# output1.to_csv('mergedFrames.csv')
# displaying result
print(output1)
