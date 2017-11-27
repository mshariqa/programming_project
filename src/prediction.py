#Author : Mohammad Shariq Azam

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import utils

def prediction(company_details):
	utils.cls()
	print("\n"+"="*23+"Prediction Screen"+"="*23)
	#get the value of from and to date from user
	from_dte, to_dte = utils.get_date()
	#intialized step as single day
	step = timedelta(days=1)
	#initializing X_train and y_train as numpy array
	X_train = np.array([])
	y_train = np.array([])
	while(from_dte <= to_dte):
		from_date=datetime.strftime(from_dte, '%d-%b-%y')
		elem = company_details[company_details['Date'].str.match(from_date, case=False)]
		if(len(elem)):
			X_train = np.append(X_train,datetime.strptime(elem.Date.values[0], '%d-%b-%y').toordinal())
			y_train = np.append(y_train,elem.Close.values[0])
		from_dte += step
	n = len(X_train)
	X_train = np.reshape(X_train,(n,1))

	#Training polynomial linear regression
	poly_reg = PolynomialFeatures(degree = 4)
	X_poly = poly_reg.fit_transform(X_train)
	poly_reg.fit(X_poly, y_train)
	polyregressor = LinearRegression()
	polyregressor.fit(X_poly, y_train)
	plt.plot(X_train, polyregressor.predict(poly_reg.fit_transform(X_train)), color = 'green', label='Polynomial Linear Regression')

	#Training linear regression using X_train and y_train
	regressor = LinearRegression()
	regressor.fit(X_train, y_train)

	#Calculating RMSE
	polyRMSE = mean_squared_error(y_train, polyregressor.predict(poly_reg.fit_transform(X_train)))
	polyR2 = r2_score(y_train, polyregressor.predict(poly_reg.fit_transform(X_train)))

	#Calculating RMSE
	RMSE = mean_squared_error(y_train, regressor.predict(X_train))
	R2 = r2_score(y_train, regressor.predict(X_train))

	#Ploting the graph for scattered training data and linear regression line
	plt.plot_date(X_train, y_train, color = 'red')
	plt.plot(X_train, regressor.predict(X_train), color = 'blue', label='Linear Regression')
	plt.title('Time vs Price (Trend)')
	plt.xlabel('Time')
	plt.ylabel('price')

	#Check if RMSE <= polyRMSE of linear regression and polynomial linear regression
	if RMSE <= polyRMSE:
		plt.figtext(0.2, 0.8, 'RMSE : {0:.2f}'.format(RMSE), fontsize=14, weight = 'bold', color = 'purple')
		plt.figtext(0.2, 0.75,'R2      : {0:.2f}'.format(R2), fontsize=14, weight = 'bold', color = 'purple')
		plt.legend(loc='upper right')
		plt.show()

	else:
		plt.figtext(0.2, 0.8, 'polyRMSE : {0:.2f}'.format(polyRMSE), fontsize=14, weight = 'bold', color = 'purple')
		plt.figtext(0.2, 0.75,'polyR2      : {0:.2f}'.format(polyR2), fontsize=14, weight = 'bold', color = 'purple')
		plt.legend(loc='upper right')
		plt.show()

	try:
		X_test = utils.check_date_after().toordinal()
		y_predlin = regressor.predict(X_test)
		y_predpoly = polyregressor.predict(poly_reg.fit_transform(X_test))

		if float(y_predlin) < 0:
			y_predlin = 0
		if float(y_predpoly) < 0:
			y_predpoly = 0

		print("\nThe linear regression predicted price for this date is            : {}".format(y_predlin[0]))
		print("\nThe polynomial linear regression predicted price for this date is : {}".format(y_predpoly[0]))

	except ValueError:
		print("\nEntered date is not in format dd-mmm-yy. Please try again ... ")
