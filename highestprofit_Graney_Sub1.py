import pandas as pd

data_csv = pd.read_csv('data.csv')
print(len(data_csv))

df = pd.DataFrame(data_csv)

InvalidIndex = df[ df['Profit (in millions)'] == 'N.A.'].index

df.drop(InvalidIndex , inplace=True)

print(len(df))

df.to_json (r'data2.json')

df.sort_values(by=['Profit (in millions)'], inplace=True, ascending=False)

dfTOP20 = df.head(20)

print(dfTOP20)
