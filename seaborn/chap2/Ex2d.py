import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a DataFrame from student data csv file
student_data = pd.read_csv("https://assets.datacamp.com/production/repositories/3996/datasets/61e08004fef1a1b02b62620e3cd2533834239c90/student-alcohol-consumption.csv")

# Print the head of df
#print(student_data.describe())

#print(student_data.sample(9))

sns.relplot(x="G1", y="G3", data=student_data,
            kind="scatter", col="schoolsup",
            col_order=["yes", "no"])

# Show plot
plt.show()
