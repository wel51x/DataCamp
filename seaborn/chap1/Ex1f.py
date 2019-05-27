import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")

sns.scatterplot(x="total_bill", y="tip",
                data=tips, hue="smoker",
                hue_order=["Yes", "No"])

plt.show()
