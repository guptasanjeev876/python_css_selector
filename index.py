import requests
import bs4
import webbrowser
from bs4 import BeautifulSoup 

url= "https://prefeitura.pbh.gov.br/saude/licitacao/pregao-eletronico-151-2020"
r = requests.get(url)

soup = bs4.BeautifulSoup(r.content, 'html.parser')

print(soup.select(".lbl-licitacao"))
