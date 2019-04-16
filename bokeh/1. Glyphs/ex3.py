# Import figure from bokeh.plotting
from bokeh.plotting import figure, ColumnDataSource
#from datetime import *

# Import output_file and show from bokeh.io
from bokeh.io import output_file, show

import numpy as np
import pandas as pd

data_dir = "/Users/wel51x/Box Sync/MyBox/Code/DataCamp/bokeh/Data/"
output_dir = "/Users/wel51x/Box Sync/MyBox/Code/DataCamp/bokeh/Output/"

# Create array using np.linspace: x
x = np.linspace(0, 5, 100)

# Create array using np.cos: y
y = np.cos(x)

# Add circles at x and y
p = figure(y_axis_label='cos(x)')
p.circle(x, y)

# Specify the name of the output file and show the result
output_file(output_dir+'ex3numpy.html')
show(p)

# Read in the CSV file: df
#df = pd.read_csv('autos.csv')
df = pd.read_csv(data_dir+'auto.csv')

# Create the figure: p
#p = figure(x_axis_label='Displacement', y_axis_label='MPG')
p = figure(x_axis_label='Horsepower', y_axis_label='MPG', title="Horsepower vs MPG")
p.title.align='center'

# Plot mpg vs hp by color
#p.circle(df.displacement, df.mpg, color=df['color'], size=10)
p.circle(df.hp, df.mpg, color=df['color'], size=10)

# Specify the name of the output file and show the result
output_file(output_dir+'ex3auto-df.html')
show(p)

# Read in the CSV file: df
df = pd.read_csv(data_dir+'medals.csv')

# Create a ColumnDataSource from df: source
source = ColumnDataSource(df)

# Add circle glyphs to the figure p
p = figure(x_axis_label='Year', y_axis_label='Time', title="Olymic 100m Dash Historic Times")
p.title.align='center'
p.circle('Year', 'Time', source=source, color='color', size=8)

# Specify the name of the output file and show the result
output_file(output_dir+'ex3sprint.html')
show(p)
