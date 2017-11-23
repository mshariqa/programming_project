from datetime import datetime, timedelta, date
#import pandas as pd

def get_date():
    while True:
        try:
            from_date = input("Please enter the From date in format dd-mon-yy. ie 20-Feb-17: ")
            from_dte = datetime.strptime(from_date,'%d-%b-%y')
            cur_dte =  datetime.strptime(str(date.today()),'%Y-%m-%d')
            if from_dte > cur_dte:
                print("From date cannot be greater than today's date.")
            else:
        	    break

        except ValueError:
               print("Invalid format")
               break

    while True:
        try:
           to_date = input("Please enter the To date in format dd-mon-yy. ie 20-Feb-17: ")
           to_dte = datetime.strptime(to_date,'%d-%b-%y')
           cur_dte =  datetime.strptime(str(date.today()),'%Y-%m-%d')
           if to_dte > cur_dte:
               print("To date cannot be greater than today's date.")
           elif to_dte < from_dte:
               print("To date cannot be less than from date.")
           else:
        	   break

        except ValueError:
           print("Invalid format")
    return from_dte, to_dte
