import pandas

df = pandas.read_csv('zadanie1.csv')
print(df)

df['data_urodzenia'] = pandas.to_datetime(df['data_urodzenia'])
limit = df['data_urodzenia'] > '1999-12-31'

birth_after_limit = len(df[limit]['data_urodzenia'])
print(f'Number of people that were born after 1999-12-31: {birth_after_limit}')

names = df['imie'].values.tolist()
female_names = set()
for n in names:
    if n[-1] == 'a':
        female_names.add(n)

print(f'All female names: {female_names}')
print(f'Total number of female names: {len(female_names)}')

