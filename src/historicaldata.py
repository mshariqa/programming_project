import utils
import pandas as pd
from datetime import datetime, timedelta, date

def historicaldata(companylist,comindex):
	ticker = companylist.iloc[int(comindex)].Symbol
	company_details = pd.read_csv("https://www.google.com/finance/historical?output=csv&q={}".format(ticker))
	step = timedelta(days=1)
	df2 = pd.DataFrame()
	from_dte,to_dte = utils.get_date()
	while(from_dte <= to_dte):
		from_date=datetime.strftime(from_dte, '%d-%b-%y')
		df = company_details[company_details['Date'].str.match(from_date, case=False)]
		df2 = df2.append(df)
		from_dte += step
	print(df2)
