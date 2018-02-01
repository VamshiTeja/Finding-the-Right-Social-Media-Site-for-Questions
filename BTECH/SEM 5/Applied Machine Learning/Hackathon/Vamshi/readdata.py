# -*- coding: utf-8 -*-
# @Author: vamshiteja
# @Date:   2017-11-18 07:50:22
# @Last Modified by:   vamshi
# @Last Modified time: 2017-11-18 19:04:51

import pandas as pd
import numpy as np
import sklearn
import datetime
import matplotlib.pyplot as plt

from matplotlib import pyplot as plt

from tensorflow.contrib import learn
from sklearn.metrics import mean_squared_error, mean_absolute_error
from lstm_predictor import lstm_model

train_file = "./train_aWnotuB.csv"
test_file  = "./test_BdBkkAj.csv"

header = ["DateTime", "Junction","Vehichles", "ID"]

## This function takes in input the date in the format(yyyy-mm-dd) and returns the day
def tell_day(dt):
    year, month, day = (int(x) for x in dt.split('-'))
    ans = datetime.date(year, month, day)
    return ans.strftime("%w")

def read(file_dir):
	df = pd.read_csv(file_dir,header=0,names=header)
	#plt.plot(df['Vehichles'])
	Days,Year,Month,Date,Hours = [],[],[],[],[]

	for dt in df['DateTime']:
		dt_ = dt
		dt = dt.split(" ")[0]
		time = dt_.split(" ")[1]
		hour = time.split(":")[0]
		Hours.append(int(hour))
		year, month, day = (int(x) for x in dt.split('-'))
		Year.append(int(year))
		Month.append(int(month))
		Date.append(int(day))
		day = tell_day(dt)
		Days.append(day)
	
	df['DateTime'] = df['DateTime'].astype('datetime64[ns]')
	#Add new columns
	df = pd.DataFrame(df)
	
	df = df.assign(Year=Year)
	df = df.assign(Month=Month)
	df = df.assign(Date=Date)
	df = df.assign(Hour = Hours)
	#df = df.assign(day= Days)

	del df['ID']
	del df['DateTime']
	vech = df['Vehichles']
	del df['Vehichles']
	df = df.assign(Vehichles=vech)

	rolling_mean = pd.rolling_mean(df['Vehichles'], window=7)
	#plt.plot(rolling_mean)
	#plt.show()
 	return df 

#This func splits input based on junctions
def split(df):
	matrix = df.as_matrix()
	j1 , j2, j3, j4 = [],[],[],[]
	for i in range(matrix.shape[0]):
		if(matrix[i][0]==1):
			j1.append(matrix[i])
		elif(matrix[i][0]==2):
			j2.append(matrix[i])
		elif(matrix[i][0]==3):
			j3.append(matrix[i])
		elif(matrix[i][0]==4):
			j4.append(matrix[i])
	j1,j2,j3,j4 = np.vstack(j1),np.vstack(j2),np.vstack(j3),np.vstack(j4)
	return j1,j2,j3,j4
	

df = read(train_file)

X1,X2,X3,X4 = split(df)

def split_train(X,y):
	l = X.shape
	train_X = X[0:10000]
	train_y = y[0:10000]
	val_X = X[10000:]
	val_y = y[10000:]
	return train_X,val_X,train_y,val_y

X_tr,X_val, y_tr, y_val = split_train(X1[:,1:4], X1[:,5])


def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
	"""
	Frame a time series as a supervised learning dataset.
	Arguments:
		data: Sequence of observations as a list or NumPy array.
		n_in: Number of lag observations as input (X).
		n_out: Number of observations as output (y).
		dropnan: Boolean whether or not to drop rows with NaN values.
	Returns:
		Pandas DataFrame of series framed for supervised learning.
	"""
	n_vars = 1
	df = pd.DataFrame(data)
	cols, names = list(), list()
	# input sequence (t-n, ... t-1)
	for i in range(n_in, 0, -1):
		cols.append(df.shift(i))
		names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
	# forecast sequence (t, t+1, ... t+n)
	for i in range(0, n_out):
		cols.append(df.shift(-i))
		if i == 0:
			names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
		else:
			names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
	# put it all together
	agg = pd.concat(cols, axis=1)
	agg.columns = names
	# drop rows with NaN values
	if dropnan:
		agg.dropna(inplace=True)
	return agg

#print y_tr
t = 7
series_data_tr = series_to_supervised(y_tr,t)
series_data = series_data_tr.as_matrix()
#print series_data[0]
X_series_tr = series_data[:][0:(t-1)]
y_series_tr = series_data[:][(t-1)]


series_data_val = series_to_supervised(y_val,t)
series_data = series_data_val.as_matrix()
X_series_val = series_data[:][0:(t-1)]
y_series_val = series_data[:][(t-1)]



LOG_DIR = './ops_logs/lstm_weather'
TIMESTEPS = 7
RNN_LAYERS = [{'num_units': 5}]
DENSE_LAYERS = [7,7]
TRAINING_STEPS = 100000
BATCH_SIZE = 100
PRINT_STEPS = TRAINING_STEPS / 100

regressor = learn.SKCompat(learn.Estimator(
    model_fn=lstm_model(
        TIMESTEPS,
        RNN_LAYERS,
        DENSE_LAYERS
    ),
    model_dir=LOG_DIR
))


# create a lstm instance and validation monitor
validation_monitor = learn.monitors.ValidationMonitor(X_series_val, y_series_val,
                                                     every_n_steps=PRINT_STEPS,
                                                     early_stopping_rounds=1000)
regressor.fit(X_series_tr, y_series_tr,
              monitors=[validation_monitor],
              batch_size=BATCH_SIZE,
              steps=TRAINING_STEPS)

y_pred = regressor.predict(X_val)

erro = mean_squared_error(y_val, y_pred)