#Author: Isha Srivastava

from datetime import datetime, timedelta, date
import subprocess as sp
#Clear the console screen
def cls():
  tmp = sp.call('cls',shell = True)

#Get to and from date in dd-mon-yy format
def get_date():
    while True:
        try:
            from_date = input("\nPlease enter the From date in format dd-mon-yy. ie 20-Feb-17: ")
            from_dte = datetime.strptime(from_date,'%d-%b-%y')
            cur_dte =  datetime.strptime(str(date.today()),'%Y-%m-%d')
            if from_dte > cur_dte:
                print("\nFrom date cannot be greater than today's date.")

            else:
              break

        except ValueError:
            print("\nInvalid date: Please try again ...")


    while True:
        try:
           to_date = input("\nPlease enter the To date in format dd-mon-yy. ie 20-Feb-17  : ")
           print("\n")
           to_dte = datetime.strptime(to_date,'%d-%b-%y')
           cur_dte =  datetime.strptime(str(date.today()),'%Y-%m-%d')
           if to_dte > cur_dte:
               print("\nTo date cannot be greater than today's date.")
           elif to_dte < from_dte:
               print("\nTo date cannot be less than from date.")
           else:
             break

        except ValueError:
           print("\nInvalid date: Please try again ...")

    return from_dte, to_dte

#Check if the predict date is greater than the current date
def check_date_after():
    while True:
        try:
            pred_date = input("Please enter the prediction date in format dd-mon-yy. ie 20-Feb-18: ")
            pred_dte = datetime.strptime(pred_date,'%d-%b-%y')
            cur_dte =  datetime.strptime(str(date.today()),'%Y-%m-%d')
            if pred_dte < cur_dte:
                print("\nPrediction date cannot be before today's date.")
            else:
              break

        except ValueError:
               print("\nInvalid date: Please try again ...")
    return pred_dte
