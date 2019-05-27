import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a DataFrame from mpg csv file
mpg = pd.read_csv("https://assets.datacamp.com/production/repositories/3996/datasets/e0b285b89bdbfbbe8d81123e64727ff150d544e0/mpg.csv")

# Create line plot
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line")

# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line", ci="sd")

# Change to create subgroups for country of origin
sns.relplot(x="model_year", y="horsepower",
            data=mpg, kind="line", ci=None,
            style="origin", hue="origin",
            markers=True)

# Show plot
plt.show()
