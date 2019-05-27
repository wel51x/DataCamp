import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")

hue_colors = {"Yes": "red",
              "No": "blue"}
hue_colors = {"Yes": "#ff0000",
              "No": "#008000"}

sns.scatterplot(x="total_bill", y="tip",
                data=tips, hue="smoker",
                palette=hue_colors)

plt.show()
