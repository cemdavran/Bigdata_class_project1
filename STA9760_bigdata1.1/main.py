from sodapy import Socrata
import json
import argparse
import os

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
		
		if output == False:
			for i in data1:
				print(i)
		#Save data into output file
		else:
			for i in data1:
				json.dump(i, f)
				f.write('\n')
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





