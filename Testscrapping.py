
from bs4 import BeautifulSoup
import pandas as pd

import requests

response = requests.get("https://www.amazon.fr/Champion-Graphic-T-Shirt-11-12-Gar%C3%A7on/dp/B08SJD3Y57/ref=sr_1_3")
soup = BeautifulSoup(response.text)
print(soup.find("div"))


