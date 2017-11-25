#Author : Mohammad Shariq Azam

import pandas as pd
from datetime import datetime, timedelta, date
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
import utils

def graph(companylist, comindex):
	print("="*20,"Graph Screen","="*20)
	while True:
		utils.cls()
		print("Select options:")
		print("1. Last 7 days")
		print("2. Last 1 month")
		print("3. Last 3 months")
		print("4. Last 6 months")
		print("5. Last 1 year")
		print("6. Go back to previous menu")
		print("7. Exit")
		option = input("Your option: ")
		if option == '1':
			step = timedelta(days=7)
			break
		elif option == '2':
			step = timedelta(days=30)
			break
		elif option == '3':
			step = timedelta(days=90)
			break
		elif option == '4':
			step = timedelta(days=180)
			break
		elif option == '5':
			step = timedelta(days=365)
			break
		elif option == '6':
			return
		elif option == '7':
			print("Thanks for coming. Please visit again ...")
			exit()
		else:
			print("Wrong option. Try again ...")

	tickerName = companylist.iloc[int(comindex)].Symbol
	dateparse = lambda dates: pd.datetime.strptime(dates, '%d-%b-%y')
	company_details = pd.read_csv("https://www.google.com/finance/historical?output=csv&q={}".format(tickerName), parse_dates=[0], index_col=[0],date_parser=dateparse)
	company_details = company_details.sort_index(ascending=True)
	while True:
		print("Select options for time series : ")
		print("1. Time series for close price ")
		print("2. Time series for volume ")
		print("3. Exit ")
		option2 = input("Your option: ")
		if option2 == '1':
			N = input("Enter the window for moving averages : ")
			ts = company_details['Close']
			tsw = company_details['Volume']
			break
		elif option2 == '2':
			N = input("Enter the window for moving averages : ")
			ts = company_details['Volume']
			tsw = company_details['Close']
			break
		elif option2 == '3':
			print("Thanks for coming. Please visit again ...")
			exit()
		else:
			print("Wrong option. Try again ...")

	cur_dte = date.today()
	cur_date = datetime.strftime(cur_dte, '%Y-%m-%d')
	from_dte = cur_dte - step
	from_date = datetime.strftime(from_dte, '%Y-%m-%d')
	ts = ts[from_date:cur_date]
	tsw = tsw[from_date:cur_date]
	N = int(N)
	rolmean = pd.Series.rolling(ts, window=N).mean()
	rolstd = pd.Series.rolling(ts, window=N).std()
	#Calculate weighted rolling mean
	wrolmean = wrolfun(ts,tsw,from_dte,cur_dte, N)
	#Calculate macd
	px = pd.DataFrame(columns=['26 ema','12 ema','MACD'])
	px['26 ema'] = pd.Series.ewm(ts, span = 26).mean()
	px['12 ema'] = pd.Series.ewm(ts, span = 12).mean()
	px['MACD'] = px['12 ema'] - px['26 ema']
	plt.figure(1)
	plt.subplot(211)
	plt.plot(ts, color='blue',label='Original')
	plt.plot(rolmean, color='red',label='Rolling Mean')
	plt.plot(wrolmean['Time'],wrolmean['Roll'], color='green',label='Weighted Rolling Mean')
	if option2 == 1:
		plt.ylabel('Price')
	elif option2 == 2:
		plt.ylabel('Volume')
	plt.xlabel('Time')
	plt.legend(loc='best')
	plt.title('Time Series plot')
	plt.figure(1)
	plt.subplot(212)
	plt.plot(rolstd, color='black',label='Rolling Standard')
	plt.plot(px['MACD'], color='green',label='MACD')
	plt.show()

def wavg(d, w):
    try:
        return (d * w).sum() / w.sum()
    except ZeroDivisionError:
        return d.mean()

def wrolfun(ts,tsw, from_dte, cur_dte,N):
	wrolmean = pd.DataFrame(columns=['Time','Roll'])
	step = timedelta(days=N)	
	timeSeries = np.array([])
	while(from_dte + timedelta(days=N) <= cur_dte):
		from_date = datetime.strftime(from_dte, '%Y-%m-%d')
		mov_from_date = datetime.strftime(from_dte + timedelta(days=N), '%Y-%m-%d')
		wrolmean = wrolmean.append(pd.Series([mov_from_date, wavg(ts[from_date:mov_from_date], tsw[from_date:mov_from_date])], index=['Time','Roll']), ignore_index=True)
		from_dte += step
	return wrolmean