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

def menu2(companylist,comindex):
	utils.cls()	
	print("*" * 80)
	loop = True
	while loop:
		print("You selected :")
		print((companylist.iloc[int(comindex)]))
		print("*" * 80)
		print("Select options:")
		print("1. Summary")
		print("2. Graph")
		print("3. Historical Data")
		print("4. Future Prediction")
		print("5. Go back to previous menu")
		print("6. Exit")
		option = input("Your option: ").lstrip()
		if option == '1':
			summary(companylist,comindex)
		elif option == '2':
			graph(companylist,comindex),
		elif option == '3':
			historicaldata(companylist,comindex),
		elif option == '4':
			prediction(companylist,comindex),
		elif option == '5':
			menu()
		elif option == '6':
			print("Thanks for coming. Please visit again ...")
			loop = False
			exit()
		else:
			print("Wrong option. Try again ...")


def name():
	utils.cls()
	companylist = pd.read_csv("http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchan0ge=nasdaq&render=download")
	companyName = input("Enter the company name you want to search:").lstrip()
	outlen = len(companylist[companylist['Name'].str.contains(companyName,case = False)])

	try:

		while(outlen > 20 or outlen < 1):
			if outlen < 1:
				print("No result found. Please try again ...")
				companyName = input("Enter the company name you want to search:").lstrip()
				outlen = len(companylist[companylist['Name'].str.contains(str(companyName),case = False)])		
			elif outlen > 20:
				print("The matching patterns are more than 20. Please enter more characters...")
				companyName = input("Enter the company name you want to search:").lstrip()
				outlen = len(companylist[companylist['Name'].str.contains(companyName,case = False)])

		print(companyName)
		temp_match = companylist[companylist['Name'].str.contains(companyName,case = False)]
		print(temp_match)
		#print(companylist.dtypes)

		loop = True
		while loop:
			comindex = int(input("Enter the index number of the company you want:").lstrip())
			if temp_match.index.contains(comindex):
				loop = False
				menu2(companylist,comindex)
			else:
				print("The name you have entered is not found. Please try again...")

	except ValueError:
			print("\nIncorrect Index Value! Please try again ... ")




def ticker():
	utils.cls()
	companylist = pd.read_csv("http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchan0ge=nasdaq&render=download")
	companyTicker = input("Enter the company ticker you want to search:").lstrip()
	matchTicker = companylist[companylist['Symbol'].str.contains(companyTicker,case = False)]
	outlen = len(matchTicker)

	try:

		while(outlen > 20 or outlen < 1):
			if outlen < 1:
				print("No result found. Please try again ...")
				companyTicker = input("Enter the company ticker you want to search:").lstrip()
				matchTicker = companylist[companylist['Symbol'].str.contains(companyTicker,case = False)]
				outlen = len(matchTicker)		
			elif outlen > 20:
				print("The matching patterns are more than 20. Please enter more characters...")
				companyTicker = input("Enter the company ticker you want to search:").lstrip()
				matchTicker = companylist[companylist['Symbol'].str.contains(companyTicker,case = False)]
				outlen = len(matchTicker)

		print(companyTicker)
		temp_match = companylist[companylist['Symbol'].str.contains(companyTicker,case = False)]
		print(temp_match)

		loop = True

		while loop:
			comindex = int(input("Enter the index number of the company you want:").lstrip())
			if temp_match.index.contains(comindex):
				loop = False
				menu2(companylist,comindex)
			else:
				print("The ticker you have entered is not found. Please try again...")

	except ValueError:
			print("\nIncorrect Index Value! Please try again ... ")



def menu():
	utils.cls()
	loop = True
	while loop:
		print("Search stock using:")
		print("1. Name")
		print("2. Ticker")
		print("3. Exit")
		option = input("Your option: ").lstrip()
		if option == '1':
			name()
		elif option == '2':
			ticker(),
		elif option == '3':
			print("Thanks for coming. Please visit again ...")
			loop = False
			exit()
		else:
			print("Wrong option. Try again ...")
menu()