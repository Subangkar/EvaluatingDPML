import pandas as pd
from sklearn.model_selection import train_test_split
df = pd.read_csv('census_all_str_short.csv')


def ratio_of_val(dframe, col, val):
    return round(len(dframe[dframe[col]==val])/len(dframe), 3)

print(ratio_of_val(df, 'PINCP', '>90K'))

train, test = train_test_split(df, test_size=0.75)
print('Train: (>90K)', ratio_of_val(train, 'PINCP', '>90K'))
print('Train: (<=90K)', ratio_of_val(train, 'PINCP', '<=90K'))
print('Test: (>90K)', ratio_of_val(test, 'PINCP', '>90K'))
print('Test: (<=90K)', ratio_of_val(test, 'PINCP', '<=90K'))

train.to_csv(f'census_short_{len(train)}.csv', index=False)
test.to_csv(f'census_short_{len(test)}.csv', index=False)