import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")
'''
hue_colors = {"Yes": "red",
              "No": "blue"}
hue_colors = {"Yes": "#ff0000",
              "No": "#008000"}
'''
sns.relplot(x="total_bill", y="tip",
            data=tips, kind="scatter",
            size="size", hue="size")

sns.relplot(x="total_bill", y="tip", data=tips,
            kind="scatter", hue="smoker", style="smoker")

# Set alpha to be between 0 and 1
sns.relplot(x="total_bill", y="tip", data=tips,
            kind="scatter", alpha=0.4)

plt.show()
