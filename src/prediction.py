import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import utils

def prediction(companylist,comindex):
	print("="*20,"Prediction Screen","="*20)
	tickerName = companylist.iloc[int(comindex)].Symbol
	company_details = pd.read_csv("https://www.google.com/finance/historical?output=csv&q={}".format(tickerName))
	from_dte, to_dte = utils.get_date()
	step = timedelta(days=1)
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
		print("The predicted price for this date is : {}".format(y_pred))
	except ValueError:
		print("Entered value is not in format dd-mmm-yy. Please try again ... ")
