import pandas as pd
import numpy as np
import matplotlib
# get_ipython().run_line_magic('matplotlib', 'inline')
# %matplotlib inline

import matplotlib.pylab as plt
from IPython import get_ipython
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

file = 'consumption_small.txt'

def parse_file(file):

	dateparse = lambda dates: pd.datetime.strptime(dates, '%d/%m/%Y %H:%M:%S')
	data = pd.read_csv(file, sep=';', parse_dates=[['Date', 'Time']], index_col=0, date_parser=dateparse, dtype={'Global_active_power': pd.np.float64}, na_values=['?'])

	# print data.head()

	# print '\n Data Types: '
	# print data.dtypes

	ts = data['Global_active_power']
	print ts.head(10)

	# ts['Global_active_power']

	# plt.plot(ts)
	ts.plot(kind='line')

	plt.show()
	return ts

from statsmodels.tsa.stattools import adfuller
def test_stationarity(timeseries):
    
    #Determing rolling statistics
    rolmean = timeseries.rolling(window=12, center=False).mean()
    rolstd = timeseries.rolling(window=12, center=False).std()

    #Plot rolling statistics:
    orig = timeseries.plot(color='blue',label='Original')
    mean = rolmean.plot(color='red', label='Rolling Mean')
    std = rolstd.plot(color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show()
    
    #Perform Dickey-Fuller test:
    print 'Results of Dickey-Fuller Test:'
    dftest = adfuller(timeseries)
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print dfoutput



def main():
	ts = parse_file('consumption_small.txt')
	test_stationarity(ts)


main()
