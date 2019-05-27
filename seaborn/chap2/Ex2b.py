import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")

sns.relplot(x="total_bill", y="tip",
            data=tips, kind = "scatter",
            col="day", col_wrap=2)

plt.show()
