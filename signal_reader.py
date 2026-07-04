import pandas as pd

file_01 = pd.read_csv('momentum.csv')
file_02 = pd.read_csv('volume.csv')

file_merge = pd.merge(file_01, file_02)

file_merge['Signals'] = file_merge.apply(lambda x: 'Buy' if x['Change'] > 0 and x['Volume'] == 'High' else 'Sell' if
										 x['Change'] < 0 and x['Volume'] == 'High' else 'Watch', axis=1)
print(file_merge)
sells = file_merge[file_merge['Signals'] == 'Sell']
print('\n',sells)
