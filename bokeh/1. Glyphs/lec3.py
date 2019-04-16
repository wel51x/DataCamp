from bokeh.io import output_file, show
from bokeh.plotting import figure
import numpy as np
from bokeh.sampledata.iris import flowers

data_dir = "/Users/wel51x/Box Sync/MyBox/Code/DataCamp/bokeh/Data/"
output_dir = "/Users/wel51x/Box Sync/MyBox/Code/DataCamp/bokeh/Output/"

#numpy
x = np.linspace(0, 10, 1000)
y = np.sin(x) + np.random.random(1000) * 0.2

plot = figure(y_axis_label='np.sin(x) + np.random.random(1000) * 0.2')
plot.line(x, y)

# Specify the name of the file & plot it
output_file(output_dir+'lec3numpy.html')
show(plot)

# Pandas

plot = figure(x_axis_label='Petal Length', y_axis_label='Sepal Length')
plot.circle(flowers['petal_length'], flowers['sepal_length'], size=10)

# Specify the name of the file & plot it
output_file(output_dir+'lec3pandas.html')
show(plot)
