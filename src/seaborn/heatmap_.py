from cheatsheets.datasets.sklearn_datasets import boston
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

boston_df = pd.DataFrame(boston.data, columns=boston.feature_names)

sns.set_theme(style="white")
corr = boston_df.corr().round(1)
mask = np.triu(np.ones_like(corr, dtype=bool), 1)
cmap = sns.diverging_palette(230, 20, as_cmap=True)  # 'RdBu_r'

f, ax = plt.subplots(figsize=(8, 8))
sns.heatmap(
    data=corr,
    mask=mask,
    annot=True,
    vmin=-1,
    vmax=1,
    center=0,
    cmap=cmap,
    square=True,
    cbar_kws={"shrink": 1}, )
plt.show()
