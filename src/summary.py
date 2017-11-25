import pandas as pd
#from summary import summary
#from graph import graph
#from historicaldata import historicaldata
#from prediction import prediction
import subprocess as sp

def mean_price(n, companydata):
    av = 0
    for i in range (n):
        av = av + companydata.at[i,'Close']  
    return av/n   

def std_dev(companydata):
    m = companydata['Close']
    num_items = len(m)
    mean = mean_price(num_items, companydata)
    diff = [x - mean for x in m]
    sq_diff = [d*d for d in diff]
    ssd = sum(sq_diff)    
    return (ssd/num_items)**(1/2)

def summary(companylist, comindex):

    tickerName = companylist.iloc[int(comindex)].Symbol  
    companydata = pd.read_csv("https://www.google.com/finance/historical?output=csv&q=" + str(tickerName))       
    print("*"*80 + "\nStock Summary:                              ")    
    today_open = companydata.at[0,'Open']
    print("Yesterday's Open Price:                     " + str(today_open))   
    today_close = companydata.at[0,'Close']
    print("Yesterday's Close Price:                    " + str(today_close))  
    today_high = companydata.at[0,'High']
    print("Yesterday's High Price:                     " + str(today_high)) 
    today_low = companydata.at[0,'Low']
    print("Yesterday's Low Price:                      " + str(today_low))  
    today_vol = companydata.at[0,'Volume']
    print("Yesterday's Volume Traded:                  " + str(today_vol))
    print("\n***Descriptive Statistics:*")
    print("7 Day Mean Close Price:                     " + str(mean_price(7, companydata)))
    print("30 Day Mean Close Price:                    " + str(mean_price(30, companydata)))
    quartiles = companydata.Close.quantile([0.25, 0.50, 0.75, 1])
    print("1st Quartile (Close Price):                 " + str(quartiles.loc[0.25]))
    print("2nd Quartile (Close Price):                 " + str(quartiles.loc[0.50]))
    print("3rd Quartile (Close Price):                 " + str(quartiles.loc[0.75]))
    print("4th Quartile (Close Price):                 " + str(quartiles.loc[1]))
    print("Range of Closing Price (Annual):            " + str(companydata['Close'].max() - companydata['Close'].min()))
    print("Standard Deviation in Close Price (Annual): " + str(std_dev(companydata)))
    print("Coefficient of Variation (Annual):          " + str(std_dev(companydata)/mean_price(len(companydata['Close']), companydata)))
    print("*"*80)