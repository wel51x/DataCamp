# Import Matplotlib, Pandas, and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Create a DataFrame from csv file
df = pd.read_csv("http://assets.datacamp.com/production/repositories/3996/datasets/ab13162732ae9ca1a9a27e2efd3da923ed6a4e7b/young-people-survey-responses.csv")

# Create a count plot with "Spiders" on the x-axis
sns.countplot(x="Spiders", data=df)

# Display the plot
plt.show()
