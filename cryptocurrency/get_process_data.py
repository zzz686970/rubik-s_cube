# -*- coding: utf-8 -*-
# @Author: zhizhong
# @Date:   2020-09-17 21:58:15
# @Last Modified by:   zhizhong
# @Last Modified time: 2020-09-28 18:37:24
import requests
import pandas as pd
import matplotlib.pyplot as plt
import io
from datetime import datetime, timedelta 


API_KEY="M99S38YJYSKRDSEY"


def get_data(url, endpoint,symbol = None, market = None, api_key = API_KEY, datatype = 'csv'):
	"""Retrieve the historical time series data
	
	parse in url, endpoint and api_key
	
	Arguments:
		url {str} -- Alphavantage api
		endpoint {str} -- Daily Digital & Crypto Currencies
		symbol {str} -- Digital/crypto currency
		market {str} -- Exchange market
	
	Keyword Arguments:
		api_key {str} -- api key stored in sys env (default: {API_KEY})
	"""
	params = {
		'function': endpoint,
		'symbol': symbol,
		'market': market,
		'apikey': api_key,
		'datatype': datatype
	}
	resp = requests.get(url, params = params)
	resp.raise_for_status()
	df = pd.read_csv(io.StringIO(resp.content.decode('utf-8') ))
	
	## save data for test
	# df.to_csv('raw_data.csv', index = False)
	# with open('raw_data.json', 'w', encoding = 'utf-8') as f:
	# 	json.dump(data, f, indent = 4)

	return df

def calculate_price(df = None):
	"""calculate close price based on requirement
	
	convert json to DataFrame for process.
	1. compute average price of each week
	2. compute 3-day and 7-day rolling average report
	
	Arguments:
		df {[dict]} -- [stock price]
	"""
	# with open('raw_data.json', 'r') as f:
	# 	json_data = json.load(f)
	# df = pd.DataFrame.from_dict(json_data)

	## df = pd.read_csv('raw_data.csv')

	## convert timestamp as date type
	df['timestamp'] = pd.to_datetime(df['timestamp'])
	# group by week_date for all dates
	df['week_date'] = df.apply(lambda row: row['timestamp'] - timedelta(days=row['timestamp'].weekday()), axis=1)
	weekly_average_df = df.groupby(df['week_date'])['close (USD)'].mean().reset_index().sort_values('week_date')
	visualize_result(weekly_average_df, 'weekly_average.png')

	## compute 7 day rolling window for closed price
	df['7day'] = df[['timestamp', 'close (USD)']].rolling(window=7).mean()
	day7_rolling_df = df[['timestamp','7day']].dropna()
	visualize_result(day7_rolling_df, '7day_rolling.png')

	## compute 3 day rolling window for closed price
	df['3day'] = df[['timestamp', 'close (USD)']].rolling(window=3).mean()
	day3_rolling_df = df[['timestamp','3day']].dropna()
	visualize_result(day3_rolling_df, '3day_rolling.png')

def visualize_result(data, file_name):
	plt.figure()
	fig = data.plot(x=data.columns[0], y=data.columns[1], marker='.', kind= 'line')
	fig.get_figure().savefig(file_name)

if __name__ == '__main__':
	### Get symbol BTC as market 'USD'

	url='https://www.alphavantage.co/query'
	endpoint = 'DIGITAL_CURRENCY_DAILY'
	df = get_data(url, endpoint, symbol = 'BTC', market = 'USD')
	calculate_price(df)





