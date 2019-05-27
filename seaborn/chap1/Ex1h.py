import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")

hue_colors = {"Male": "red",
              "Female": "blue"}
'''
hue_colors = {"Yes": "#ff0000",
              "No": "#008000"}
'''
sns.countplot(x="smoker", data=tips,
              hue="sex", palette=hue_colors)

plt.show()
