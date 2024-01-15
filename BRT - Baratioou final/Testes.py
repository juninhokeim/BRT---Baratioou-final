import requests
from bs4 import BeautifulSoup

link = "https://www.mercadolivre.com.br/samsung-galaxy-a14-4g-64gb-4gb-verde-lima/p/MLB22396561?pdp_filters=deal:MLB779362-2&hide_psmb=true"
headers = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
requisicao = requests.get(link)

site = BeautifulSoup(requisicao.text, "html.parser")

titulo = site.find("title")
#print(titulo)
print(titulo.get_text())

precoNormal = site.find_all("span", class_="andes-money-amount__fraction")
precoNormal = precoNormal[0].get_text()

resultado = precoNormal #+","+ centavos
print("R$" + " "+ resultado + ",00") 

precoPromo = site.find_all("span", class_="andes-money-amount__fraction")
precoPromo = precoPromo[1].get_text()
centavos = site.find_all("span", class_="andes-money-amount__cents")
centavos = centavos[0].get_text()

resultado = precoPromo +","+ centavos
print("R$" + " " + resultado)

oferta = site.find("div", class_="ui-pdp-promotions-pill-label", string="OFERTA DO DIA")

if oferta:
    print("ATENÇÃO: Oferta do dia!")
    # Se quiser obter o texto dentro da tag div, você pode usar oferta.get_text()
    # print(oferta.get_text())
else:
    print("OFERTA DO DIA não encontrada.")