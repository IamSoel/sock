from bs4 import BeautifulSoup
from bs4 import NavigableString
import requests
import pandas as pd

def scrape_listedcompanies():
    url='http://www.nepalstock.com/company/index/?_limit=400'
    page=requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
    soup=BeautifulSoup(page.content,'html.parser')
    names=soup.select("tr.unique td")
    columnlist=[]
    for i in names:
        columnlist.append(i.text)
    df=pd.DataFrame(columns=columnlist)

    rows=soup.find("table", attrs={"class":"table"}).find_all("tr")[2:-1]
    number=len(rows)
    for i in range (2,number+2):
        rows=soup.find("table", attrs={"class":"table"}).find_all("tr")[i]
        l=[]
        td=rows.find_all('td')
        for i in td:
            if i.find('a', href=True):
                for a in i.find_all('a', href=True):
                    l.append(a['href'])
            else:
                l.append(i.text.strip())
                
        a_series = pd.Series(l, index = df.columns)
        df = df.append(a_series, ignore_index=True)

    listedCompanies = df.to_json(orient = 'records')
    # print(listedCompanies)
scrape_listedcompanies()

