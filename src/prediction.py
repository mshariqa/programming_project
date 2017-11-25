#Author : Mohammad Shariq Azam

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import utils

def prediction(companylist,comindex):
	utils.cls()
	print("\n"+"="*23+"Prediction Screen"+"="*23)
	tickerName = companylist.iloc[int(comindex)].Symbol
	company_details = pd.read_csv("https://www.google.com/finance/historical?output=csv&q={}".format(tickerName))
	#get the value of from and to date from user
	from_dte, to_dte = utils.get_date()
	#intialized step as single day
	step = timedelta(days=1)
	#initializing X_train and y_train as numpy array
	X_train = np.array([])
	y_train = np.array([])
	while(from_dte <= to_dte):
		from_date=datetime.strftime(from_dte, '%d-%b-%y')
		df = company_details[company_details['Date'].str.match(from_date, case=False)]
		if(len(df)):
			X_train = np.append(X_train,datetime.strptime(df.Date.values[0], '%d-%b-%y').toordinal())
			y_train = np.append(y_train,df.Close.values[0])
		from_dte += step
	n = len(X_train)
	X_train = np.reshape(X_train,(n,1))
	#Training linear regression using X_train and y_train 
	regressor = LinearRegression()
	regressor.fit(X_train, y_train)

	plt.plot_date(X_train, y_train, color = 'red')
	plt.plot(X_train, regressor.predict(X_train), color = 'blue')
	plt.title('Time vs Price (Training set)')
	plt.xlabel('Time')
	plt.ylabel('price')
	plt.show()

	try:
		X_test = utils.check_date_after().toordinal() 
		y_pred = regressor.predict(X_test)
		if float(y_pred) < 0:
			y_pred = 0
		print("\nThe predicted price for this date is : {}".format(y_pred))
	except ValueError:
		print("\nEntered value is not in format dd-mmm-yy. Please try again ... ")
