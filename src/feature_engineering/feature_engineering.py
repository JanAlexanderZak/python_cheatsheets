""" Data Cleaning and Feature Engineering
"""
import numpy as np
import pandas as pd
import re
desired_width = 320
pd.set_option('display.width', desired_width)
pd.options.display.float_format = '{:.2f}'.format
pd.options.display.min_rows = 3
pd.options.display.max_rows = 50
pd.options.display.max_columns = 10
pd.options.display.precision = 5
# pd.reset_option('expand_frame_repr')

df = pd.read_csv('data/countries_of_the_world/countries of the world.csv', delimiter=',', decimal=',')

# OVERVIEW
print(df.head())
print(df.tail())
print(df.sample())
print(df.columns)
print(df.count(axis='columns'))
print(df.count(axis='rows'))
print(df.shape)
print(df.dtypes)
print(df.info)
print(df.describe())
print(df.describe(include=[np.number]))
print(df.describe(include=[object]))
print(df.describe(exclude=[object]))
print(df.value_counts())
print(df['Region'].value_counts())
print(df.select_dtypes(include=['int64']))
print(df.select_dtypes(include=[np.number]))

# missing
print(df.isnull().sum())
df.fillna(value=np.nan, inplace=True)
print(df.isnull().sum())

# CLEANING
# Clean string columns
df['Country'] = df['Country'].str.replace('[a-zA-Z]', ' ')  # clean hyphens and other special chars


columns = [
    'Country', 'Region', 'Population', 'Area (sq. mi.)', 'Pop. Density (per sq. mi.)',
    'Coastline (coast/area ratio)', 'Net migration', 'Infant mortality (per 1000 births)', 'GDP ($ per capita)',
    'Literacy (%)', 'Phones (per 1000)', 'Arable (%)', 'Crops (%)', 'Other (%)', 'Climate', 'Birthrate', 'Deathrate',
    'Agriculture', 'Industry', 'Service']
# Rename specific columns
df.rename(columns={
    '': ''},
    inplace=True)

# Reformat columns
df.columns = df.columns.str.strip()
df.columns = df.columns.str.lower()
df.columns = [re.sub(r' ', '', str(x)) if isinstance(x, str) else x for x in df.columns]
df.columns = [re.sub(r'\([^)]*\)', '', str(x)) if isinstance(x, str) else x for x in df.columns]
df.columns = [re.sub(r'\.', '_', str(x)) if isinstance(x, str) else x for x in df.columns]
print(df.columns)
print(df)

# Check for whitespaces
print(repr(df['country'][0]))
print(repr(df['region'][0]))
df['country'] = df['country'].str.strip()
df['region'] = df['region'].str.strip()
print(repr(df['country'][0]))
print(repr(df['region'][0]))


# Convert to numeric
def to_numeric(old):
    new = old.replace(',', '.')
    return float(new)


df["gdp"] = df["gdp"].astype(str)
df["gdp"] = df["gdp"].apply(to_numeric)
df["netmigration"] = df["netmigration"].astype(str)
df["netmigration"] = df["netmigration"].apply(to_numeric)

# FEATURE ENGINEERING
# Summarize sum of categorical values under threshold
counts = df['region'].value_counts()
mask = df['region'].isin(counts[counts < 20].index)
df['region'][mask] = 'other'
print(pd.value_counts(df['region']))

# Binarize numerical column over threshold
df['binary_population'] = 0
df.loc[df['population'] > 50000000, 'binary_population'] = 1

# todo: combine binarize and sum of values ?

# Bin numerical columns with inf
df['bins_population'] = pd.cut(
    df['population'],
    bins=[-np.inf, 0, 50000000, np.inf],
    labels=['low', 'med', 'high'], )


# Cross features
print(df.columns)
df_ = pd.crosstab(df['bins_population'], df['region'])
print(df_)


# Bin categorical columns
def bin_countries(row):
    # Optionally strip
    if row['country'].strip() in ['Afghanistan']:
        print("Found Afghanistan!")
        return 'Is_Afghanistan'
    else:
        return 'Not_Afghanistan'


df['bins_country'] = df.apply(lambda row: bin_countries(row), axis=1)
print(df.info())

# Sting columns
# get char len, ... all string funcs
df['len_country'] = df['country'].str.len()
df['country'] = df['country'].str.zfill(10)

# One-Hot encoding // dummy (drops 1st)
df = pd.get_dummies(df, columns=['region'], prefix='region')

# Skaling
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))
# or loop over columns
scaler.fit(df[['population']])
df['normalized_population'] = scaler.transform(df[['population']])
print(df['normalized_population'].describe())

# Quantiles
lower, upper = df['population'].quantile([0.05, 0.95])
new_df = df[(df['population'] < upper) & (df['population'] > lower)]

# Std dev
mean = df['population'].mean()
std = df['population'].std()
cut_off = std * 3
lower, upper = mean - cut_off, mean + cut_off
new_df = df[(df['population'] < upper) & (df['population'] > lower)]

# Create Features
df['migration_per_pop'] = df.apply(lambda row: row['netmigration'] / row['population'] * 10000, axis=1)
print(df.sample(10))

""" Feature engineering
- Extract useful features from raw data
- Replace missing values (median, sigma, std, arbitrary)
- Numeric: Scaling (MinMaxScaler / StandardScaler), calculate new feature, bins
- Categorical: one-hot, hashing, name by count/index
- Cross features
- Visualize with heatmap
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import random
import os
from sklearn.feature_selection import VarianceThreshold, chi2, f_classif, SelectKBest
from sklearn.feature_selection import SelectPercentile
from cheatsheets.datasets.sklearn_datasets.sklearn_datasets import iris
pd.options.display.float_format = "{:,.2f}".format

# Load iris dataset
features = iris.data
target = iris.target

# Load weight-height dataset
file_path = os.path.join(os.path.dirname(__file__), '..', 'datasets', 'weight_height', 'weight-height.csv')
df_weight_height = pd.read_csv(file_path, sep=',')
df_weight_height = df_weight_height.rename(columns={"Height": "Height_(in)", "Weight": "Weight_(lbs)"})
print("Samples: \n", df_weight_height.sample())
print("dtypes: \n", df_weight_height.dtypes)
print("Shape: \n", df_weight_height.shape)
print("Info: \n", df_weight_height.info())
print("Description: \n", df_weight_height.describe())

# Create BMI feature
df_weight_height['Height_(m)'] = df_weight_height['Height_(in)'] / 39.37
df_weight_height['Weight_(kg)'] = df_weight_height['Weight_(lbs)'] / 2.205
df_weight_height['BMI_(kg/m^2)'] = df_weight_height.apply(
    lambda row: row['Weight_(kg)'] / (row['Height_(m)'] ** 2), axis=1)
df_weight_height['BMI_(703in/lbs^2)'] = df_weight_height.apply(
    lambda row: 703 * row['Weight_(lbs)'] / (row['Height_(in)'] ** 2), axis=1)

df_weight_height['High_BMI'] = df_weight_height['BMI_(kg/m^2)'] > 25
print(df_weight_height.sample())

# Percentiles
lower_percentile, upper_percentile = df_weight_height['Height_(m)'].quantile([0.05, 0.95])
print(lower_percentile, upper_percentile)
print(df_weight_height[(df_weight_height['Height_(m)'] < lower_percentile) | (df_weight_height['Height_(m)'] > upper_percentile)])

# Using sklearn
percentile_selector = SelectPercentile(f_classif, percentile=0.95)
features_selected = percentile_selector.fit_transform(features, target)
print(features_selected)

# 3 sigma
_mean = df_weight_height['Height_(m)'].mean()
_std = df_weight_height['Height_(m)'].std()
upper_sigma = _mean + (3 * _std)
lower_sigma = _mean - (3 * _std)
print(lower_sigma, upper_sigma)
print(df_weight_height[(df_weight_height['Height_(m)'] < lower_sigma) | (df_weight_height['Height_(m)'] > upper_sigma)])

# Cross features
df = pd.crosstab(df_weight_height['High_BMI'], df_weight_height['Gender'], normalize=True, margins=True)
print(df)
sns.heatmap(data=df, annot=True, cbar=False, cmap="YlGnBu")
plt.show()

# Create bins
bins = [0, 1.7, 2.0, 99.0]
df = pd.cut(
    df_weight_height['Height_(m)'],
    bins,
    labels=['>0.0m', '>1.7m', '>2.0m'])
print(df)
print(pd.value_counts(df))

# One hot encoding
df_weight_height = pd.get_dummies(df_weight_height)
print(df_weight_height.columns)

# Hashing values
df_weight_height['Hash'] = df_weight_height['Gender_Male'].apply(hash)
print(df_weight_height)

"""
A1:     b, a
A2:     float
A3:     float
A4:     u, y, l, t
A5:     g, p, gg
A6:     c, d, cc, i, j, k, m, r, q, w, x, e, aa, ff
A7:     v, h, bb, j, n, z, dd, ff, o
A8:     float
A9:     t, f
A10:    t, f
A11:    float
A12:    t, f
A13:    g, p, s
A14:    float
A15:    float
A16:    +,-
"""

# Load data
columns = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16']
file_path = os.path.join(os.path.dirname(__file__), '..', 'datasets', 'credit_approval_uci', 'crx.csv')
df = pd.read_csv(file_path, names=columns)

# Reformat columns
df = df.replace('?', np.nan)
df['A16'] = df['A16'].map({'+': 1, '-': 0})
NUMERIC_COLUMNS = ['A2', 'A3', 'A8', 'A11', 'A15']
CATEGORICAL_COLUMNS = ['A1', 'A4', 'A5', 'A6', 'A7', 'A9', 'A10', 'A12', 'A13']

# Describe
print(df.sample())
print(df.tail())
print(df.describe())

# Create random noise
values = [random.randint(0, len(df) - 1) for i in range(0, 99)]
for column in NUMERIC_COLUMNS:
    df.loc[values, column] = np.nan

# Find missing values
print("Missing values (ordered): \n", df.isnull().mean().sort_values(ascending=True))
sns.heatmap(df.isna())
plt.show()

# Replace with median
# All numeric columns
for column in NUMERIC_COLUMNS:
    value = df[column].median()
    df[column] = df[column].fillna(value)


# Replace with mode
# Mode is the median of categorical
for column in CATEGORICAL_COLUMNS:
    value = df[column].mode()[0]
    df[column] = df[column].fillna(value)

# Visualize result
sns.heatmap(df.isna())
plt.show()

# Declare as missing
for column in CATEGORICAL_COLUMNS:
    df[column].fillna('Missing', inplace=True)

# Replace missing value with arbitrary value
# np.where: condition, if true, if false
pd.to_numeric(df['A2'])
lower_percentile, upper_percentile = df['A2'].quantile([0.05, 0.95])
df['A2'] = np.where(
    df['A2'] > upper_percentile, 99, df['A2'])

# Ordinal mapping of one column
ordinal_mapping = {k: i for i, k in enumerate(
    df['A4'].unique(), 0)}
print(ordinal_mapping)
print(df.columns)

# Count mapping of one column
count_map = df['A4'].value_counts().to_dict()
print(count_map)
print(df.columns)

# One hot encoding
df = pd.get_dummies(df[CATEGORICAL_COLUMNS], drop_first=True)
print(df.sample())
print(df.columns)

# Variance thresholding
thresholder = VarianceThreshold(threshold=0.66)
features_threshold = thresholder.fit_transform(features)
print(features_threshold)
print("Variances: ", thresholder.fit(features).variances_)


# Chi selector
features = features.astype(int)
chi2_selector = SelectKBest(chi2, k=2)  # use f_classif if categorical
features_chi2 = chi2_selector.fit_transform(features, target)
print(features.shape[1], features_chi2.shape[1])
