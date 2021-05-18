import requests
import bs4


url= "https://prefeitura.pbh.gov.br/saude/licitacao/pregao-eletronico-151-2020"
data = requests.get(url)

soup = bs4.BeautifulSoup(data.content, 'html.parser')

print(soup.select(".lbl-licitacao"))

for links in soup.find_all('a'):
    link = links.get('href')
    print(link)