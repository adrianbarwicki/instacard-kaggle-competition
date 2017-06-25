import numpy as numpy
import pandas as pd

## Reading data
cols_names = [ 'order_id', 'user_id', 'eval_set', 'order_number', 'order_dow', 'order_hour_of_day', 'days_since_prior_order' ]

orders = pd.read_csv('./data/orders.csv', sep=',', names=cols_names, encoding='latin-1')

print orders