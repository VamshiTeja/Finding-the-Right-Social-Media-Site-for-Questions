# -*- coding: utf-8 -*-
# @Author: vamshi
# @Date:   2017-11-18 13:08:38
# @Last Modified by:   vamshi
# @Last Modified time: 2017-11-18 14:47:56

import tensorflow as tf
import pandas
import numpy as np 
from matplotlib import pyplot as plt

from tensorflow.contrib import learn
from sklearn.metrics import mean_squared_error, mean_absolute_error
from lstm_predictor import generate_data, load_csvdata, lstm_model






regressor = learn.Estimator(model_fn=lstm_model(TIMESTEPS, RNN_LAYERS, DENSE_LAYERS), 
                                      n_classes=0,
                                      verbose=1,  
                                      steps=TRAINING_STEPS, 
                                      optimizer='Adagrad',
                                      learning_rate=0.03, 
                                      batch_size=BATCH_SIZE)




validation_monitor = learn.monitors.ValidationMonitor(X['val'], y['val'],
                                                      every_n_steps=PRINT_STEPS,
                                                      early_stopping_rounds=1000)

regressor.fit(X['train'], y['train'], monitors=[validation_monitor], logdir=LOG_DIR)


predicted = regressor.predict(X['test'])
mse = mean_absolute_error(y['test'], predicted)
print ("Error: %f" % mse)

plot_predicted, = plt.plot(predicted, label='predicted')
plot_test, = plt.plot(y['test'], label='test')
plt.legend(handles=[plot_predicted, plot_test])
