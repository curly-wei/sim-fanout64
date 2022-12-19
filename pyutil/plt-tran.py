import pandas as pd
import matplotlib.pyplot as plt
import getopt
import sys

def us_scaler(arr):
	return [x*pow(10,6) for x in arr]

def mv_scaler(arr):
	return [x*pow(10,3) for x in arr]

vo_data = None
vi_data = None
x_axis_name = 't(us)'
y_axis_name = 'Amplitude(mV)'

vo_data_t = []
vo_data_v = []

argv = sys.argv[1:]
try:
	opts, args = getopt.getopt(argv, "i:o:")
except:
	print("Error")


for opt, arg in opts:
	if opt in ['-o']:
		vo_data = pd.read_csv(\
			arg, \
			sep='\s+', \
			header=None, \
			usecols=[0,1], \
			names=[x_axis_name, y_axis_name]
		)				
	if opt in ['-i']:
		vi_data = pd.read_csv(\
			arg, \
			sep='\s+', \
			header=None, \
			usecols=[0,1], \
			names=[x_axis_name, y_axis_name]
		)	
## 1. Plot refer to here
## https://tinyurl.com/app/myurls
## 2. Why usecols=is [1,3] rather than [1,2]
## Depend on your OS, ngspice version..etc. env.
## Some env. is [1,3], some env. is [1,2]

vo_data_t = us_scaler(vo_data[x_axis_name])
vo_data_v = mv_scaler(vo_data[y_axis_name])
vi_data_t = us_scaler(vi_data[x_axis_name])
vi_data_v = mv_scaler(vi_data[y_axis_name])

plt.plot(\
	vo_data_t,\
	vo_data_v,\
	label='Vo'\
)
plt.plot(\
	vi_data_t,\
	vi_data_v,\
	label='Vi, R/F time = 20ns, pulse width = 1us'\
)

plt.xlabel(x_axis_name)
plt.ylabel(y_axis_name)
plt.title('Vi & Vo of 48 channels fanout: '+ argv[1] )
plt.legend()
plt.show()