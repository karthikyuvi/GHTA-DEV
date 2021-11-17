import requests
from requests.auth import HTTPDigestAuth
import json
import os


js_loop = "for( i=0 ;i< document.getElementsByClassName('{0}').length;i++){{ document.getElementsByClassName('{0}')[i].innerHTML = '{1}'; }}"
def js_line(value1, value2):
	try:
		l = js_loop.format(value1, value2)
		return l
	except Exception as e:
		print(e)
		print(values[0], " Not updated!!")
	return " "

api_username = os.environ.get('API_USERNAME')
api_password = os.environ.get('API_PASSWORD')
session = requests.Session()
session.auth = (api_username, api_password)

auth = session.post("http://public.etfg.com/v2/public_disclosures")
response = session.get("http://public.etfg.com/v2/public_disclosures")


r_content = json.loads(response.content.decode('utf-8'))
if r_content['response']['status_description'] != 'Success':
	pass

date_of_info = list(r_content['data'].keys())[0]
fund_info = r_content['data'][date_of_info][0]




prev_nav = 0
with open("assets/old_cache.txt",'r') as f:
	for line in f:
		prev_nav = float(line.strip("\n|\r"))

with open("assets/js/etf1_python.js",'w') as f:
	f.write(js_line('fund_ticker',fund_info['fund_ticker']))
	f.write(js_line('fund_description',fund_info['fund_description']))
	f.write(js_line('fund_iopv',fund_info['iopv_symbol']))
	f.write(js_line('fund_exchg',fund_info['fund_listing_exchange']))
	f.write(js_line('fund_cusip',fund_info['fund_cusip']))
	f.write(js_line('fund_inception_date',fund_info['inception_date']))
	f.write(js_line('fund_net_assets',"${:,.2f}".format(float(fund_info['fund_shares_outstanding'])*float(fund_info['nav']))))
	f.write(js_line('fund_shares_ots',"{:,}".format(fund_info['fund_shares_outstanding'])))

	f.write(js_line('fund_info_date',date_of_info))
	f.write(js_line('fund_nav',fund_info['nav']))
	f.write(js_line('fund_close_price',fund_info['market_price']))
	f.write(js_line('fund_discount_premium',fund_info['discount_premium']))
	f.write(js_line('fund_thirty_day_median_bid_ask',fund_info['thirty_day_median_bid_ask']))

	if prev_nav == 0:
		f.write(js_line('fund_chg_dollar',0.0))
		f.write(js_line('fund_chg_percent',0.0))
	else:
		f.write(js_line('fund_chg_dollar', float(fund_info['nav']) - prev_nav))
		f.write(js_line('fund_chg_percent', (float(fund_info['nav']) - prev_nav)/prev_nav))

	f.write(js_line('premium_discount_days_q', fund_info['premium_discount_days_q'] ))
	f.write(js_line('premium_discount_days_y', fund_info['premium_discount_days_y'] ))

	f.write(js_line('current_cal_q_pd_premium', fund_info['current_cal_q_pd_premium'] ))
	f.write(js_line('current_cal_q_pd_discount', fund_info['current_cal_q_pd_discount'] ))
	f.write(js_line('current_cal_q_pd_total', fund_info['current_cal_q_pd_total'] ))

	f.write(js_line('previous_cal_y_pd_premium', fund_info['previous_cal_y_pd_premium'] ))
	f.write(js_line('previous_cal_y_pd_discount', fund_info['previous_cal_y_pd_discount'] ))
	f.write(js_line('previous_cal_y_pd_total', fund_info['previous_cal_y_pd_total'] ))

	holding_tr = ""
	for i in range(0,len(fund_info['constituents'])):
		holding_info = fund_info['constituents'][i]
		holding_tr += "<tr>"
		holding_tr += "<td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td>".format(holding_info['as_of_date'],holding_info['constituent_description'],holding_info['constituent_ticker'],holding_info['constituent_cusip'],holding_info['constituent_market_value'],holding_info['shares_held_of_constituent'],holding_info['constituent_weight'])
		holding_tr += "</tr>"
	##Holdings table
	'''
	for loop to create all the table rows for holdings
	'''
	f.write('document.getElementById("fund_holdings_table").innerHTML += "{}";'.format(holding_tr))
	# print(holding_tr)

with open("assets/old_cache.txt",'w') as f:
	f.write(str(fund_info['nav']))
