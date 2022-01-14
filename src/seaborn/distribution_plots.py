import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

# Displot
sns.displot(tips['total_bill'], kde=True, bins=100)
plt.show()

# Jointplot
sns.jointplot(x='total_bill', y='tip', data=tips, kind='scatter')
sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')
sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde')
sns.jointplot(x='total_bill', y='tip', data=tips, kind='reg')
plt.show()

# Add plots
g = sns.jointplot(x='total_bill', y='tip', data=tips, kind='scatter')
g.plot_joint(sns.kdeplot, color="r", zorder=0, levels=6)
g.plot_marginals(sns.rugplot, color="r", height=-.15, clip_on=False)
plt.show()

# Pairplot
sns.pairplot(tips, hue='sex', palette='coolwarm')
plt.show()
