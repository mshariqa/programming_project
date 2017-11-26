#Author: Isha Srivastava

import utils
import pandas as pd
from datetime import datetime, timedelta, date

def summary(step, company_details):
    df2 = pd.DataFrame()
    from_dte,to_dte= utils.get_date()
    while(from_dte <= to_dte):
        from_date=datetime.strftime(from_dte, '%#d-%b-%y')
        df = company_details[company_details['Date'].str.match(from_date, case=False)]
        df2 = df2.append(df)
        df2 = df2.reset_index(drop=True)
        from_dte += step[0]
    if len(df2) < 1:
        print ("Sorry! No results found for the given date range.\n")
    else:
        print("="*20+"History"+"="*20+"\n\n"+str(df2)+"\n\n"+"="*48)

def summary_monthly(company_details):
    df2 = pd.DataFrame()
    df_summary = pd.DataFrame()
    step = timedelta(days=1)
    from_dte,to_dte = utils.get_date()
    while(from_dte <= to_dte):
        from_date=datetime.strftime(from_dte, '%#d-%b-%y')
        df = company_details[company_details['Date'].str.match(from_date, case=False)]
        df2 = df2.append(df)
        from_dte += step
    df2 = df2[::-1]
    df2 = df2.reset_index(drop=True)
    df_summary = df2.head(1)
    for i in range (len(df2)-1):
        date = datetime.strptime(df2.loc[i][0], '%d-%b-%y')
        next_date = datetime.strptime(df2.loc[i+1][0], '%d-%b-%y')
        if (date.month != next_date.month):
            df_summary = df_summary.append(df2.loc[i+1])
    df_summary = df_summary.reset_index(drop=True)
    if len(df_summary) < 1:
        print ("Sorry! No results found for the given date range.\n")
    else:
        print("="*16+"Monthly history"+"="*16+"\n\n"+str(df_summary)+"\n\n"+"="*47)

def freq_menu(company_details):
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

def historicaldata(company_details):
    freq_menu(company_details)