# PROCESS 
# 1. DWFE: done.
# 2. Waiting...

# IMPORT PACKAGES
import matplotlib as mpl
import matplotlib.pyplot as plt

## Why so?
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

## Chinese font
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

# PLOT FOR TIME SEIRES

## single plot with specific figure size - option one
plt.rcParams['figure.figsize'] = (6, 4)
fig, ax = plt.subplots(1, 1)
ax.plot(x, y)  # general plot
ax.plot_date(datetime_series, value_series, '-', color='tab:orange', label='test') # time series plot

## single plot with specific figure size - option two
plt.figure(figsize=(6, 4))
ax = plt.subplot(111)
ax.plot...

## Double y-axis
fig, ax1 = plt.subplots(1, 1)
ax1.plot_date(datetime_series, value_series, '-', color='tab:orange', label='test')
ax2 = plt.twinx(ax1)
ax2.plot_date(datetime_series, value_series, '-', color='tab:orange', label='test')

## Multiple subplot
fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
ax1.plot...
ax2.plot...
ax3.plot...

## Attributes

### figure size, legend, label, title, grid
ax.legend(loc=1)
ax.set_xlabel('x')
ax.set_title(title_name)
ax.grid()

### time-tick format
from matplotlib.dates import DateFormatter
formatter = DateFormatter('%H:%m')
ax.xaxis.set_major_formatter(formatter)

### adjustment
plt.tight_layout()

## save and close
plt.savefig(file_name, quality=95, dpi=500) # save current figure in default
plt.close() # close all figures
