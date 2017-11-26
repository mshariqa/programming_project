#Author: Isha Srivastava

import utils
import pandas as pd
from datetime import datetime, timedelta, date

# This function displays the historical data within the date range given by the user
def summary(step, company_details):
    hist_data = pd.DataFrame()
    from_dte,to_dte= utils.get_date()
    while(from_dte <= to_dte):
        from_date=datetime.strftime(from_dte, '%#d-%b-%y')
        hist_data = hist_data.append(company_details[company_details['Date'].str.match(from_date, case=False)])
        hist_data = hist_data.reset_index(drop=True)
        from_dte += step[0]
    to_date=datetime.strftime(to_dte, '%#d-%b-%y')
    if not len(hist_data[hist_data['Date'].str.match(to_date, case=False)]):
        hist_data = hist_data.append(company_details[company_details['Date'].str.match(to_date, case=False)])
        hist_data = hist_data.reset_index(drop=True)
    if len(hist_data) < 1:
        print ("Sorry! No results found for the given date range.\n")
    else:
        print("="*20+"History"+"="*20+"\n\n"+str(hist_data)+"\n\n"+"="*48)

# This function displays the historical  on monthly frequency basis within the date range given by the user
def summary_monthly(company_details):
    hist_data = pd.DataFrame()
    month_summary = pd.DataFrame()
    step = timedelta(days=1)
    from_dte,to_dte = utils.get_date()
    while(from_dte <= to_dte):
        from_date=datetime.strftime(from_dte, '%#d-%b-%y')
        hist_data = hist_data.append(company_details[company_details['Date'].str.match(from_date, case=False)])
        from_dte += step
    hist_data = hist_data[::-1]
    hist_data = hist_data.reset_index(drop=True)
    month_summary = hist_data.head(1)
    for i in range (len(hist_data)-1):
        date = datetime.strptime(hist_data.loc[i][0], '%d-%b-%y')
        next_date = datetime.strptime(hist_data.loc[i+1][0], '%d-%b-%y')
        if (date.month != next_date.month):
            month_summary = month_summary.append(hist_data.loc[i+1])
    month_summary = month_summary.reset_index(drop=True)
    if len(month_summary) < 1:
        print ("Sorry! No results found for the given date range.\n")
    else:
        print("="*16+"Monthly history"+"="*16+"\n\n"+str(month_summary)+"\n\n"+"="*47)

# This function is used for printing the menu for frequency of data retreival
def historicaldata(company_details):
    loop = True
    utils.cls()
    while loop:
        print("\nPlease enter the Frequecy option for viewing Historical Data:")
        print("1. Daily")
        print("2. Weekly")
        print("3. Monthly")
        print("4. Go back to previous menu")
        print("5. Exit")
        option = input("\nYour option                                                 : ")
        print("\n")
        if option == '1':
            step = timedelta(days=1),
            summary(step,company_details)
        elif option == '2':
            step = timedelta(days=7),
            summary(step,company_details)
        elif option == '3':
            step = timedelta(days=30),
            summary_monthly(company_details)
        elif option == '4':
            return
        elif option == '5':
            print("Thanks for coming. Please visit again...\n")
            loop = False
            exit()
        else:
            print("Wrong option. Try again...\n")
