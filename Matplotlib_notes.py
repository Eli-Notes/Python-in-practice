# PROCESS 
# 1. DWFE: done.
# 2. Waiting...

# PLOT FOR TIME SEIRES
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()  ### Why so???

## single plot
fig, ax = plt.subplots(1, 1)
ax.plot_date(datetime_series, value_series, '-', color='tab:orange', label='test')
ax.plot(x,y)  # general plot

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

### figure size
plt.rcParams['figure.figsize'] = (7, 7)

### label, legend
ax.legend(loc=1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(title_name)

### time-tick format
from matplotlib.dates import DateFormatter
formatter = DateFormatter('%H:%m')
ax.xaxis.set_major_formatter(formatter)

### adjustment
plt.tight_layout()

## save and close
plt.savefig(file_name, quality=95, dpi=500)
plt.close()
