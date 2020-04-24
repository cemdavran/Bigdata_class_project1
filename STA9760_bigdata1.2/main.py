from sodapy import Socrata
import json
import argparse
import os
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

#Build main function to retrieve NYC data and create the output
def main(page_size, num_page, output):
	datasource = Socrata("data.cityofnewyork.us", dict(os.environ)["APP_KEY"])
	offset = 0

	#Calculates possible number of pages for dataset
	if num_page == False:
		rows = datasource.get("nc67-uf89", select='COUNT(*)')
		int_cnt = int(rows[0]['COUNT'])
		num_page = (int_cnt//page_size)+1

	#Creates output file based on user input
	if output != False:
		f = open(output, 'w')

		#Calling data from NYC Data
	for i in range(num_page):
		data1 = datasource.get("nc67-uf89", limit=page_size, offset = offset)
		
		for k in data1:
			if output == False:
				print(k)
		#Save data into output file
			else:
				json.dump(k, f)
				f.write('\n')
				
			#adjusted data for consistent data format
			k['issue_date'] = datetime.strptime(k['issue_date'],'%m/%d/%Y').date()
			if 'fine_amount' in k:
				k['fine_amount'] = float(k['fine_amount'])
				k['penalty_amount'] = float(k['penalty_amount'])
				k['interest_amount'] = float(k['interest_amount'])
				k['reduction_amount'] = float(k['reduction_amount'])
				k['payment_amount'] = float(k['payment_amount'])
				k['amount_due'] = float(k['amount_due'])


			res = es.index(index = "parking_violations", doc_type = 'json', body = k)
		offset += page_size

#Define and parse commandline arguments from user		
parser = argparse.ArgumentParser(description = 'Inputs for Parking Violation Data')
parser.add_argument('--page_size', type = int, required = True)
parser.add_argument('--num_page', type = int, default = False)
parser.add_argument('--output', type = str, default = False)

#Use the input arguments in main function
if __name__ == '__main__':
	arguments = parser.parse_args()
	main(**vars(arguments))

