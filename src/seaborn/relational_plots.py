import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

# Heatmap
sns.heatmap(tips.corr(), annot=True)
plt.show()

flights_ = flights.pivot_table(values='passengers', index='month', columns='year')
sns.heatmap(flights_)
plt.show()

# Scatter
sns.relplot(data=tips, x="total_bill", y="tip", hue="day")
plt.show()

sns.scatterplot(
    data=tips, x="total_bill", y="tip", hue="size", size="size",
    sizes=(20, 200), hue_norm=(0, 7), legend="full"
)
plt.show()


