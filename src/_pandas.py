import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt


# Setup pandas
pd.set_option('precision', 3)
pd.set_option('max_rows', 20)
pd.set_option('max_colwidth', 30)
pd.options.display.float_format = "{:,.2f}".format


# Read in and rename
file_path = 'file_path'
df = pd.read_csv(file_path, sep=',')
df = df.rename(columns={"Height": "Height_(in)", "Weight": "Weight_(lbs)"})
print("Samples: \n", df.sample())
print("dtypes: \n", df.dtypes)
print("Shape: \n", df.shape)
print("Info: \n", df.info())
print("Description: \n", df.describe())

# Create features
df['Height_(m)'] = df['Height_(in)'] / 39.37
df['Weight_(kg)'] = df['Weight_(lbs)'] / 2.205
df['BMI_(kg/m^2)'] = df.apply(
    lambda row: row['Weight_(kg)'] / (row['Height_(m)'] ** 2), axis=1)
df['BMI_(703in/lbs^2)'] = df.apply(
    lambda row: 703 * row['Weight_(lbs)'] / (row['Height_(in)'] ** 2), axis=1)

df['High_BMI'] = df['BMI_(kg/m^2)'] > 25

# Mock data for cheatsheet
labels = ['a', 'b', 'c']
list_ = [1, 2, 3]
matrix_ = np.random.rand(4, 5)
arr = np.array([1, 2, 3])
dict_ = {
    'a': [1],
    'b': [2],
    'c': [3], }
functions = [sum, print, len]


# Series
pd.Series(data=list_, index=labels)     # from array and labels
pd.Series(dict_)                        # from dictionary
pd.Series(functions)                    # from array with functions


# Dataframes
df = pd.DataFrame(
    matrix_,
    index='1 2 3 4'.split(),
    columns='A B C D E'.split(), )      # from data

pd.DataFrame(dict_)                     # from dict


# Access to df
df.shape
df.size
df.columns
df.index
df.head()
df.tail()
df.sample()
df.describe()
df.info()
df.nunique()
df.values                               # return all values
df.index                                # access index
df.columns                              # access columns
df.isnull
np.abs(df)                              # get absolute values with np
df.rank()                               # rank with index
df.index.is_unique
# df.transponse()                       # .T operation

df['A'].count()                         # .mean() .min() .max() .quartile() .unique() .value.count()
# df['A'].str.upper()                   # string manipulation
# df['A'].str.contains('string')
# df['A'].str.contains('string').sum()  # count of trues


# Boolean
df > 0                                  # >, <, ==
df[df > 0]                              # returns df
df[df['A'] > 0]                         # returns df


# Vectorized methods
df * 2                                  # +, -, *, /, **
df.div(10)
df.mul(2)
df.add(1, axis='columns')
df.sub(1, axis='columns')
df.floordiv(10)                         # divide all entries by 10
df.apply(lambda n: n//10)               # apply function


# Indexing
# [i, j[
df['A']                                 # access columns
df.A
df.loc['1']                             # access index
df.iloc[0]
df[['A', 'B']]                          # access a lis of columns
df['F'] = 0                             # create new column
df.drop('1', axis=0)                    # drop axis
df.drop('A', axis=1)                    # drop column


# Multi index
inner = ['A', 'A', 'A', 'B', 'B', 'B', ]
outer = [1, 2, 3, 1, 2, 3]
index = pd.MultiIndex.from_arrays([inner, outer])
df = pd.DataFrame(
    np.random.randn(6, 2),
    index=index,
    columns=['Column A', 'Column B'], )


# Format df
df.applymap(lambda x: '%.2f' % x)

df.reset_index()                        # set index back to numerical
# df.set_index('A B C D'.split())         # new index


# Missing values
# df.reindex('A B C D'.split(), method='ffill')
df.notna()
df.dropna(axis=1, thresh=2)             # drop complete row/column
df.fillna(value='FILL VALUE')
df.drop_duplicates()
df.replace([1, 2, 3], np.nan)


# Pivot
df = pd.DataFrame(
    {'foo': ['1', '1', '1', '2', '2', '2'],
     'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
     'baz': [1, 2, 3, 4, 5, 6], })
df_pivoted = df.pivot(
    index='foo',
    columns='bar',
    values='baz', )


# Binning
ages = [20, 22, 25, 27, 21, 23, 37]
bins = [18, 25, 35, 36]
df = pd.cut(
    ages,
    bins,
    labels=['young', 'adult', 'old'])
df.codes
df.categories
pd.value_counts(df)


# Group by
# Only with dulicates...
df = pd.DataFrame(data={
    'AA': ['A', 'A', 'B', 'B', 'C', 'C'],
    'BB': ['1', '2', '3', '4', '5',  '6'],
    'CC': [1, 2, 3, 4, 5, 6], })
by_comp = df.groupby("AA").sum()


# Merge / Join
df1 = pd.DataFrame(
    {'A': [1, 2, 99],
     'B': [1, 2, 3], },
    index=[0, 1, 2], )

df2 = pd.DataFrame(
    {'C': [1, 2, 3],
     'D': [1, 2, 3], },
    index=[0, 1, 2], )

df3 = pd.DataFrame(
    {'A': [1, 2, 3],
     'D': [1, 2, 3], },
    index=[0, 1, 2], )

pd.concat([df1, df2], axis=1)               # appends to column / row, force it with axis=1
pd.merge(df1, df3, how='inner', on='A')     # other options: inner, outer, left, right
                                            # merges like sql, only complete identical values
df1.join(df2)                               # different indexes required


# Visualize
df1['A'].plot.hist(bins=50)
df1.plot.bar(stacked=True)
df1.plot.scatter(x='A', y='B')
df1.plot.box()
df1.plot.density()
# plt.show()


# SQL
query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20),
c REAL, d INTEGER
);
"""
con = sqlite3.connect('db.sqlite')
# con.execute(query)
# con.commit()

data = [
    ('A', 'G', 1.25, 6),
    ('A', 'G', 1.25, 6),
    ('A', 'G', 1.25, 6), ]
stmt = "INSERT INTO test VALUES(?,?,?,?)"
con.executemany(stmt, data)
con.commit()

cursor = con.execute('select * from test')
rows = cursor.fetchall()

# print(cursor.description)
pd.DataFrame(rows, columns=[x[0] for x in cursor.description])


# Styling
# Format
def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = 'red' if val < 0 else 'black'
    return 'color: %s' % color


print(df.style.applymap(color_negative_red))

