import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a DataFrame from mpg csv file
mpg = pd.read_csv("https://assets.datacamp.com/production/repositories/3996/datasets/e0b285b89bdbfbbe8d81123e64727ff150d544e0/mpg.csv")

# Print the head of df
print(mpg.describe())

print(mpg.sample(9))

sns.relplot(x="horsepower", y="mpg",
            data=mpg, kind="scatter",
            size="cylinders", hue="cylinders")

sns.relplot(x="acceleration", y="mpg",
            data=mpg, kind="scatter",
            style="origin", hue="origin")

# Show plot
plt.show()
