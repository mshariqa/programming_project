#programming project
#Isha Srivastava-1720133
#Mohammad Shariq Azam-17202383
#Aman Thakur-

import pandas as pd

def name():
	companylist = pd.read_csv("http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchan0ge=nasdaq&render=download")
	companyName = input("Enter the company name you want to search:")

	print(companylist[companylist['Name'].str.match(companyName,case = False)])

	#print(companylist.head())

def ticker():
	companylist = pd.read_csv("http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchan0ge=nasdaq&render=download")
	companyTicker = input("Enter the company name you want to search:")

	print(companylist[companylist['Symbol'].str.match(companyTicker,case = False)])


def menu():

	print("Search stock using:")
	print("1. Name")
	print("2. Ticker")
	option = input("Your option: ")
	switcher =  {
		'1': name,
		'2': ticker
	}
	switcher[option]()
menu()
