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
		print("\nSelect option (1-7):")
		print("1. Last 7 days")
		print("2. Last 1 month")
		print("3. Last 3 months")
		print("4. Last 6 months")
		print("5. Last 1 year")
		print("6. Go back to previous menu")
		print("7. Exit\n")
		option = input("Your option 		                        : ")
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
			print("\nThanks for coming. Please visit again ...")
			exit()
		else:
			print()
			input("\nWrong option."+" Press Enter to continue...")

	tickerName = companylist.iloc[int(comindex)].Symbol
	#Function to parse and covert date from string to datetime for time series
	dateparse = lambda dates: pd.datetime.strptime(dates, '%d-%b-%y')
	#Function to read csv file for time series with additional parameters for parsing date in datetime format
	company_details = pd.read_csv("https://www.google.com/finance/historical?output=csv&q={}".format(tickerName), \
		parse_dates=[0], index_col=[0],date_parser=dateparse)
	#Sorted the csv data in ascending order of date
	company_details = company_details.sort_index(ascending=True)
	print("\n")
	print("="*20,"Time series option(Price/Volume)","="*20)
	while True:
		print("\nSelect options for time series (1-3): ")
		print("1. Time series for close price ")
		print("2. Time series for volume ")
		print("3. Exit ")
		option2 = input("\nYour option                                     : ")
		try:
			if option2 == '1':
				N = input("\nEnter the window in integer for moving averages : ")
				if int(N) < 2 or int(N) > int(step.days):
					print("\nWindow should be less than 2 or more than the selected time period")
				else:
					ts = company_details['Close']
					tsw = company_details['Volume']
					break
			elif option2 == '2':
				N = input("\nEnter the window in integer for moving averages : ")
				if int(N) < 2 or int(N) > int(step.days):
					print("\nWindow should be less than 2 or more than the selected time period")
				else:
					ts = company_details['Volume']
					tsw = company_details['Close']
					break
			elif option2 == '3':
				print("\nThanks for coming. Please visit again ...\n")
				exit()
			else:
				print("\nWrong option. Try again ...")
		except ValueError:
			print("\nIncorrect Format!! Please try again ... ")

	cur_dte = date.today()
	#converting date from datetime to string
	cur_date = datetime.strftime(date.today(), '%Y-%m-%d')
	#from date = current date - step
	from_dte = cur_dte - step
	#converting date from datetime to string
	from_date = datetime.strftime(from_dte, '%Y-%m-%d')
	ts = ts[from_date:cur_date]
	tsw = tsw[from_date:cur_date]
	N = int(N)
	#Calculate rolling mean
	rolmean = pd.Series.rolling(ts, window=N).mean()
	#Calculate rolling standard
	rolstd = pd.Series.rolling(ts, window=N).std()
	#Calculate weighted rolling mean
	wrolmean = wrolfun(ts,tsw,from_dte,cur_dte, N)
	#Calculate macd
	px = macd(ts)
	#Plotting graph
	fig = plt.figure()
	plt.subplot(211)
	plt.plot(ts, color='blue',label='Original')
	plt.plot(rolmean, color='red',label='Rolling Mean')
	plt.plot(wrolmean['Time'],wrolmean['Roll'], color='green',label='Weighted Rolling Mean')
	if option2 == '1':
		plt.title('Time Series plot for price')
		plt.ylabel('Price')
	elif option2 == '2':
		plt.title('Time Series plot for volume')
		plt.ylabel('Volume')
	plt.xlabel('Time')
	plt.legend(loc='upper left')
	plt.figure(1)
	plt.subplot(212)
	if option2 == '1':
		plt.ylabel('Price')
	elif option2 == '2':
		plt.ylabel('Volume')
	plt.xlabel('Time')
	plt.plot(rolstd, color='black',label='Rolling Standard')
	plt.plot(px['MACD'], color='green',label='MACD')
	plt.legend(loc='upper left')
	plt.show()

#This function calculates the weighted mean
def wavg(d, w):
    try:
        return (d * w).sum() / w.sum()
    except ZeroDivisionError:
        return d.mean()

#This function calculates the weighted rolling mean
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

#This function calculates the macd for a series
def macd(ts):
	px = pd.DataFrame(columns=['26 ema','12 ema','MACD'])
	px['26 ema'] = pd.Series.ewm(ts, span = 26).mean()
	px['12 ema'] = pd.Series.ewm(ts, span = 12).mean()
	px['MACD'] = px['12 ema'] - px['26 ema']
	return px
