
from bs4 import BeautifulSoup
import pandas as pd

import requests

response = requests.get("https://www.auchan.fr/joyeuses-fetes/idees-cadeaux/ca-13224333")
soup = BeautifulSoup(response.text,features="html.parser")
prod = soup.find_all("div",{'class' :"product-price bolder red-txt"})
print (prod)
prix_initials = []
for e in prod :
   for e in prod :
    e = e.text
    prix_initials.append (e)
    
print (prix_initials)