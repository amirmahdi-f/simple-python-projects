import requests
import bs4


def get_price ():
    site = requests.get(url="https://www.livedata.ir/")
    soup = bs4.BeautifulSoup(site.text, features="html.parser")
    
    for price in soup.select("#s_200103"):
        return(price.get_text())
        
print(f"dollar : {get_price()}")
