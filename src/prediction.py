import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.linear_model import LinearRegression

def prediction(companylist,comindex):
	tickerName = companylist.iloc[int(comindex)].Symbol
	companyInfo = pd.read_csv("https://www.google.com/finance/historical?output=csv&q={}".format(tickerName))
	i = 0
	n = len(companyInfo.Date)
	X_train = np.zeros(len(companyInfo.Date))
	y_train = np.zeros(len(companyInfo.Date))
	for date, close in zip(companyInfo.Date,companyInfo.Close):
	    X_train[i] = datetime.strptime(date, '%d-%b-%y').toordinal()
	    y_train[i] = close
	    i += 1

	X_train = np.reshape(X_train,(n,1))
	tp = np.zeros(len(companyInfo.Date))
	regressor = LinearRegression()
	regressor.fit(X_train, y_train)

	try:
		X_test = datetime.strptime(input("Input your date to predict price in format dd-mmm-yy : "), '%d-%b-%y').toordinal() 
		print(X_test)
		y_pred = regressor.predict(X_test)
		print("The predicted price for this date is : {}".format(y_pred))
	except ValueError:
		print("Entered value is not in format dd-mmm-yy. Please try again ... ")


