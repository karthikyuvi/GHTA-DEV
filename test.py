import requests
from requests.auth import HTTPDigestAuth
import json

session = requests.Session()
session.auth = ("goosehollow1", "368d49b781cf")

auth = session.post("http://public.etfg.com/v2/public_disclosures")
response = session.get("http://public.etfg.com/v2/public_disclosures")




r_content = json.loads(response.content.decode('utf-8'))
if r_content['response']['status_description'] != 'Success':
	pass

date_of_info = list(r_content['data'].keys())[0]
fund_info = r_content['data'][date_of_info][0]

js_loop = "for( i=0 ;i< document.getElementsByClassName('{0}').length;i++){{ document.getElementsByClassName('{0}')[i].innerHTML = '{1}'; }}"

with open("assets/js/etf1_python.js",'w') as f:
	f.write(js_loop.format('fund_ticker',fund_info['fund_ticker']))
	f.write(js_loop.format('fund_description',fund_info['fund_description']))
	f.write(js_loop.format('fund_iopv',fund_info['iopv_symbol']))
	f.write(js_loop.format('fund_exchg',fund_info['fund_listing_exchange']))
	f.write(js_loop.format('fund_cusip',fund_info['fund_cusip']))
	f.write(js_loop.format('fund_inception_date',fund_info['inception_date']))
	f.write(js_loop.format('fund_net_assets',"${:,.2f}".format(float(fund_info['fund_shares_outstanding'])*float(fund_info['nav']))))
	f.write(js_loop.format('fund_shares_ots',"{:,}".format(fund_info['fund_shares_outstanding'])))

	f.write(js_loop.format('fund_info_date',date_of_info))
	f.write(js_loop.format('fund_nav',fund_info['nav']))
	f.write(js_loop.format('fund_close_price',fund_info['market_price']))

	