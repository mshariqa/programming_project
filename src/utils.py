#Author: Isha Srivastava

from datetime import datetime, timedelta, date
import subprocess as sp
#Clear the console screen
def cls():
  tmp = sp.call('cls',shell = True)

#Get To and From date from user in dd-mon-yy format and validate it
def get_date():
    while True:
        try:
            from_date = datetime.strptime(input("\nPlease enter the From date in format dd-mon-yy. ie 20-Feb-17: "),'%d-%b-%y')
            cur_date =  datetime.strptime(str(date.today()),'%Y-%m-%d')
            if from_date > cur_date:
                print("\nFrom date cannot be greater than today's date.")

            else:
              break

        except ValueError:
            print("\nInvalid date or format: Please try again ...")


    while True:
        try:
           to_date = datetime.strptime(input("\nPlease enter the To date in format dd-mon-yy. ie 20-Feb-17  : "),'%d-%b-%y')
           cur_date =  datetime.strptime(str(date.today()),'%Y-%m-%d')
           if to_date > cur_date:
               print("\nTo date cannot be greater than today's date.")
           elif to_date < from_date:
               print("\nTo date cannot be less than from date.")
           else:
             break

        except ValueError:
           print("\nInvalid date or format: Please try again ...")

    return from_date, to_date

#Check if the predict date is greater than the current date
def check_date_after():
    while True:
        try:
            pred_date = datetime.strptime(input("\nPlease enter the prediction date in format dd-mon-yy. ie 20-Feb-18: "),'%d-%b-%y')
            cur_date =  datetime.strptime(str(date.today()),'%Y-%m-%d')
            if pred_date < cur_date:
                print("\nPrediction date cannot be before today's date.")
            else:
              break

        except ValueError:
               print("\nInvalid date or format: Please try again ...")
    return pred_date
