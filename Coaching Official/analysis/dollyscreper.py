import pandas as pd
import requests
from bs4 import BeautifulSoup


url=requests.get("https://www.thestartupjournal.com/stories/")
html = url.content
soup= BeautifulSoup(html,"html.parser")

main=soup.find('section', class_='section-category-posts')

data=[]

for vs in main.find_all('div', class_='post-inner entry-inner entry-data'):
    name=vs.text
    startup=    data.append({
        "Player":name})
print(data)
pd.DataFrame(data).to_csv("startup.csv")