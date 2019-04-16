from bokeh.io import output_file, show
from bokeh.plotting import figure

data_dir = "/Users/wel51x/Box Sync/MyBox/Code/DataCamp/bokeh/Data/"
output_dir = "/Users/wel51x/Box Sync/MyBox/Code/DataCamp/bokeh/Output/"

x = [1,2,3,4,5]
y = [8,6,5,2,3]

plot = figure()
plot.line(x, y, line_width=2)
plot.circle(x, y, fill_color='white', size=10)

# Specify the name of the file & plot it
output_file(output_dir+'lec2line.html')
show(plot)

# Patches
xs = [ [1,1,2,2], [2,2,4], [2,2,3,3] ]
ys = [ [2,5,5,2], [3,5,5], [2,3,4,2] ]

plot = figure()
plot.patches(xs, ys, fill_color= ['red', 'blue','green'], line_color='white')

# Specify the name of the file & plot it
output_file(output_dir+'lec2patches.html')
show(plot)
