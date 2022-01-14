import seaborn as sns
import matplotlib.pyplot as plt

# General settings
sns.set_style('white')
sns.despine()
plt.figure(figsize=(12, 3))
iris = sns.load_dataset('iris')

# Grids
g1 = sns.PairGrid(iris)             # load empty canvas
g1.map(plt.scatter)                 # populate with scatter plot

g2 = sns.PairGrid(iris)             # load empty canvas
g2.map_diag(plt.hist)               # populate ...
g2.map_upper(plt.scatter)
g2.map_lower(sns.kdeplot)
plt.show()

# Plot on grid
# .catplot is a high level api to plot on grids
# sns.catplot(data=df_weight_height, x='Gender', y='BMI_(703in/lbs^2)', hue='High_BMI', kind='box')

fig, axs = plt.subplots(ncols=2)
sns.boxplot(data=df, x='Gender', y='Weight_(kg)', ax=axs[0])
sns.boxplot(data=df, x='Gender', y='BMI_(703in/lbs^2)', hue='High_BMI', ax=axs[1])
plt.show()
