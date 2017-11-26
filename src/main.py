#Stock program
#Aman Thakur-17200128
#Isha Srivastava-17200133
#Mohammad Shariq Azam-17202383

import pandas as pd
from summary import summary
from graph import graph
from historicaldata import historicaldata
from prediction import prediction
import utils

companylist = pd.read_csv("http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchan0ge=nasdaq&render=download")

def menu2(companydata,companylist,comindex):
	utils.cls()	
	print("="*26, "You selected", "="*26)
	print((companylist.iloc[int(comindex)]))
	loop = True
	while loop:
		print("\n"+"="*25+"Stock Options"+"="*25)
		print("\nSelect options:")
		print("1. Summary")
		print("2. Graph")
		print("3. Historical Data")
		print("4. Future Prediction")
		print("5. Go back to previous menu")
		print("6. Exit")
		option = input("\nYour option:                                ").lstrip()
		if option == '1':
			summary(companydata)
		elif option == '2':
			graph(companylist,comindex),
		elif option == '3':
			historicaldata(companydata),
		elif option == '4':
			prediction(companydata),
		elif option == '5':
			menu()
		elif option == '6':
			print("\nThanks for coming. Please visit again ...\n")
			loop = False
			exit()
		else:
			print("\nWrong option. Try again ...")


def name():
	utils.cls()
	companyName = input("\nEnter the company name you want to search     : ").lstrip()
	outlen = len(companylist[companylist['Name'].str.contains(companyName,case = False)])

	while(outlen > 20 or outlen < 1):
		if outlen < 1:
			print("\nNo result found. Please try again ...")
			companyName = input("Enter the company name you want to search: ").lstrip()
			outlen = len(companylist[companylist['Name'].str.contains(str(companyName),case = False)])
		elif outlen > 20:
			print("\nThe matching patterns are more than 20. Please enter more characters...")
			companyName = input("\nEnter the company name you want to search     : ").lstrip()
			outlen = len(companylist[companylist['Name'].str.contains(companyName,case = False)])

	temp_match = companylist[companylist['Name'].str.contains(companyName,case = False)]
	print(temp_match.loc[:,'Symbol':'Name'])

	loop = True
	while loop:
		try:
			comindex = int(input("\nEnter the index number of the company you want: ").lstrip())
			if temp_match.index.contains(comindex):
				loop = False
				tickerName = companylist.iloc[int(comindex)].Symbol
				companydata = pd.read_csv("https://www.google.com/finance/historical?output=csv&q=" + str(tickerName))       
				menu2(companydata,companylist,comindex)
			else:
				print("\nThe name you have entered is not found. Please try again...")

		except ValueError:
			print("\nIncorrect Index Value! Please try again... ")

def ticker():
	utils.cls()
	companyTicker = input("\nEnter the company ticker you want to search: ").lstrip()
	matchTicker = companylist[companylist['Symbol'].str.contains(companyTicker,case = False)]
	outlen = len(matchTicker)

	while(outlen > 20 or outlen < 1):
		if outlen < 1:
			print("\nNo result found. Please try again ...")
			companyTicker = input("Enter the company ticker you want to search: ").lstrip()
			matchTicker = companylist[companylist['Symbol'].str.contains(companyTicker,case = False)]
			outlen = len(matchTicker)
		elif outlen > 20:
			print("\nThe matching patterns are more than 20. Please enter more characters...")
			companyTicker = input("\nEnter the company ticker you want to search: ").lstrip()
			matchTicker = companylist[companylist['Symbol'].str.contains(companyTicker,case = False)]
			outlen = len(matchTicker)

	temp_match = companylist[companylist['Symbol'].str.contains(companyTicker,case = False)]
	print(temp_match.loc[:,'Symbol':'Name'])

	loop = True
	while loop:
		try:
			comindex = int(input("\nEnter the index number of the company you want: ").lstrip())
			if temp_match.index.contains(comindex):
				loop = False
				tickerName = companylist.iloc[int(comindex)].Symbol
				companydata = pd.read_csv("https://www.google.com/finance/historical?output=csv&q=" + str(tickerName))
				menu2(companydata,companylist,comindex)
			else:
				print("\nThe ticker you have entered is not found. Please try again...")

		except ValueError:
			print("\nIncorrect Index Value! Please try again ... ")

def menu():
	utils.cls()
	loop = True
	while loop:
		print("="*20+"Welcome"+"="*20)
		print("\nSearch stock using:")
		print("1. Name")
		print("2. Ticker")
		print("3. Exit")
		option = input("\nYour option       : ").lstrip()
		if option == '1':
			name()
		elif option == '2':
			ticker(),
		elif option == '3':
			print("\nThanks for coming. Please visit again ...\n")
			loop = False
			exit()
		else:
			print("\nWrong option. Try again ...")
menu()