#programming project
import pandas as pd
from summary import summary
from graph import graph
from historicaldata import historicaldata
from prediction import prediction


def menu2(comindex):
	loop = True

	while loop:
		print("Watch options:")
		print("1. Summary")
		print("2. Graph")
		print("3. Historical Data")
		print("4. Future Prediction")
		print("5. Go back to previous menu")
		print("6. Exit")
		option = input("Your option: ")
		if option == '1':
			summary(comindex)
		elif option == '2':	
			graph(comindex),
		elif option == '3':	
			historicaldata(comindex),
		elif option == '4':	
			prediction(comindex),
		elif option == '5':	
			menu()
		elif option == '6':	
			print("Thanks for coming. Please visit again ...")
			exit()
		else:
			print("Wrong option. Try again ...")

def name():
	companylist = pd.read_csv("http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchan0ge=nasdaq&render=download")
	companyName = input("Enter the company name you want to search:")

	outlen = len(companylist[companylist['Name'].str.match(companyName,case = False)])
	while(outlen <= 1):
		print("No result found. Please try again ...")
		companyName = input("Enter the company name you want to search:")
		outlen = len(companylist[companylist['Name'].str.match(companyName,case = False)])

	while(outlen > 20):
		print("The matching patterns are more than 20. Please enter more characters...")
		companyName = input("Enter the company name you want to search:")
		outlen = len(companylist[companylist['Name'].str.match(companyName,case = False)])
	print(companyName)
	print(companylist[companylist['Symbol'].str.match(companyName,case = False)])
	#print(companylist.dtypes)
	comindex = input("Enter the index number of the company you want:")
	print("You selected :")
	print((companylist.iloc[int(comindex)]))
	#print((companylist.loc[int(comindex)]))
	menu2(comindex)


def ticker():
	companylist = pd.read_csv("http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchan0ge=nasdaq&render=download")
	companyTicker = input("Enter the company ticker you want to search:")

	outlen = len(companylist[companylist['Symbol'].str.match(companyTicker,case = False)])
	while(outlen <= 1):
		print("No result found. Please try again ...")
		companyTicker = input("Enter the company ticker you want to search:")
		outlen = len(companylist[companylist['Symbol'].str.match(companyTicker,case = False)])

	while(outlen > 20):
		print("The matching patterns are more than 20. Please enter more characters...")
		companyTicker = input("Enter the company ticker you want to search:")
		outlen = len(companylist[companylist['Symbol'].str.match(companyTicker,case = False)])
	
	print(companylist[companylist['Symbol'].str.match(companyTicker,case = False)])
	#print(companylist.dtypes)
	comindex = input("Enter the index number of the company you want:")
	print("You selected :")
	print((companylist.iloc[int(comindex)]))
	menu2(comindex)

def menu():
	loop = True
	while loop:
		print("Search stock using:")
		print("1. Name")
		print("2. Ticker")
		print("3. Exit")
		option = input("Your option: ")
		if option == '1':
			name()
		elif option == '2':	
			ticker(),
		elif option == '3':	
			print("Thanks for coming. Please visit again ...")
			exit()
		else:
			print("Wrong option. Try again ...")	
menu()