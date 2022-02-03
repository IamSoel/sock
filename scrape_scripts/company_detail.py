import email
from bs4 import BeautifulSoup
import requests
import json


def scrape_companydetail(url):
    page=requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}).content
    soup=BeautifulSoup(page,'html5lib')
    # name of company:name
    name_td=soup.find_all("td", class_="unique")
    for i in name_td:
        name=i.text

    # name and symbol:nameandsymbol
    nameandsymbol_td=soup.select('#company-view > table > tbody > tr:nth-of-type(5) > td:nth-of-type(2)')
    for i in nameandsymbol_td:
        nameandsymbol=i.text

    # Address of company:address
    address_td=soup.select('#company-view > table > tbody > tr:nth-of-type(6) > td:nth-of-type(2)')
    for i in address_td:
        address=i.text

    #Email company:email
    email_td=soup.select('#company-view > table > tbody > tr:nth-of-type(7) > td:nth-of-type(2)')
    for i in email_td:
        email=i.text

    #Website company:website
    website_td=soup.select('#company-view > table > tbody > tr:nth-of-type(8) > td:nth-of-type(2)')
    for i in website_td:
        website=i.text

    #Last Traded Price (Rs):lasttraded
    lasttraded_td=soup.select('#company-view > table > tbody > tr:nth-of-type(9) > td:nth-of-type(2)')
    for i in lasttraded_td:
        lasttraded=i.text

    #Change (Rs.) and (%):change
    change_td=soup.select('#company-view > table > tbody > tr:nth-of-type(10) > td:nth-of-type(2)')
    for i in change_td:
        change=i.text

    #Total Listed Shares:totallisted
    totallisted_td=soup.select('#company-view > table > tbody > tr:nth-of-type(11) > td:nth-of-type(2)')
    for i in totallisted_td:
        totallisted=i.text
    
    #Paid Up Value (Rs.):paidup
    paidup_td=soup.select('#company-view > table > tbody > tr:nth-of-type(12) > td:nth-of-type(2)')
    for i in paidup_td:
        paidup=i.text

    #Total Paid Up Value (Rs.):totalpaidup
    totalpaidup_td=soup.select('#company-view > table > tbody > tr:nth-of-type(13) > td:nth-of-type(2)')
    for i in totalpaidup_td:
        totalpaidup=i.text

    #Closing Market Price (Rs.)):closingprice
    closingprice_td=soup.select('#company-view > table > tbody > tr:nth-of-type(14) > td:nth-of-type(2)')
    for i in closingprice_td:
        closingprice=i.text

    #Market Capitalization (Rs.)):marketcapital
    marketcapital_td=soup.select('#company-view > table > tbody > tr:nth-of-type(15) > td:nth-of-type(2)')
    for i in marketcapital_td:
        marketcapital=i.text


    #creating json
    companydetail_dict={
        "name" : name,
        "nameandsymbol" : nameandsymbol,
        "address" : address,
        "email" : email,
        "website" : website,
        "lastTradedPrice" : lasttraded,
        "totalListedShares" : totallisted,
        "paidUpValue" : paidup,
        "totalPaidUpValue" : totalpaidup,
        "closingMarketPrice" : closingprice,
        "marketCapitalization" : marketcapital
        }

    companyDetail = json.dumps(companydetail_dict, indent = 4)
    # print(companyDetail)

url="http://www.nepalstock.com/company/display/2753"
scrape_companydetail(url)