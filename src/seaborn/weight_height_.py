import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
pd.options.display.float_format = "{:,.2f}".format

file_path = os.path.join(os.path.dirname(__file__), '..', 'datasets', 'weight_height', 'weight-height.csv')
df_weight_height = pd.read_csv(file_path, sep=',')
df_weight_height = df_weight_height.rename(columns={"Height": "Height_(in)", "Weight": "Weight_(lbs)"})

# Create BMI feature
df_weight_height['Height_(m)'] = df_weight_height['Height_(in)'] / 39.37
df_weight_height['Weight_(kg)'] = df_weight_height['Weight_(lbs)'] / 2.205
df_weight_height['BMI_(kg/m^2)'] = df_weight_height.apply(
    lambda row: row['Weight_(kg)'] / (row['Height_(m)'] ** 2), axis=1)
df_weight_height['BMI_(703in/lbs^2)'] = df_weight_height.apply(
    lambda row: 703 * row['Weight_(lbs)'] / (row['Height_(in)'] ** 2), axis=1)

df_weight_height['High_BMI'] = df_weight_height['BMI_(kg/m^2)'] > 25
print(df_weight_height.sample())

# Visualize
# Scatterplot
sns.set_theme()
sns.set_style("whitegrid")
markers = {False: "s", True: "X"}  # just for kicks, linear seperation line visible
ax = sns.scatterplot(data=df_weight_height, x='Height_(m)', y='Weight_(kg)', hue='Gender', style='High_BMI', markers=markers, linewidth=0, alpha=0.7)
plt.show()

# Distplot
male = df_weight_height[df_weight_height['Gender'] == 'Male']['Height_(m)']
femal = df_weight_height[df_weight_height['Gender'] == 'Female']['Height_(m)']
ax = sns.displot(df_weight_height, x='Height_(m)', hue='Gender')
plt.axvline(male.mean(), color='blue')
plt.axvline(femal.mean(), color='red')
plt.show()

# Pairplot
ax = sns.displot(data=df_weight_height, x='Height_(m)', y='Weight_(kg)', hue='Gender', alpha=0.4, rug=True)
plt.show()

# Boxplot
# High level api for grids
# sns.catplot(data=df_weight_height, x='Gender', y='BMI_(703in/lbs^2)', hue='High_BMI', kind='box')
fig, axs = plt.subplots(ncols=2)
sns.boxplot(data=df_weight_height, x='Gender', y='Weight_(kg)', ax=axs[0])
sns.boxplot(data=df_weight_height, x='Gender', y='BMI_(703in/lbs^2)', hue='High_BMI', ax=axs[1])
plt.show()
