import requests
from bs4 import BeautifulSoup

link = "https://www.mercadolivre.com.br/pilha-alcalina-aa-pequena-duracell-com-16-unidades/p/MLB19748584?pdp_filters=category:MLB7060%7Cdeal:MLB15852#searchVariation=MLB19748584&position=1&search_layout=grid&type=product&tracking_id=56f83eb1-6162-42df-bea3-6f2e5b2dbd95"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}
requisicao = requests.get(link, headers=headers)

site = BeautifulSoup(requisicao.text, "html.parser")

titulo = site.find("title")
if titulo:
    print(titulo.get_text())
else:
    print("Título não encontrado")

precoNormal = site.find_all("span", class_="andes-money-amount__fraction")
if precoNormal:
    precoNormal = precoNormal[0].get_text()
    print("Preço Normal: R$ " + precoNormal + ",00")
else:
    print("Preço Normal não encontrado")

precoPromo = site.find_all("span", class_="andes-money-amount__fraction")
if len(precoPromo) > 1:
    precoPromo = precoPromo[1].get_text()
    centavos = site.find_all("span", class_="andes-money-amount__cents")
    centavos = centavos[0].get_text()
    resultado = precoPromo + "," + centavos
    print("Preço Promocional: R$ " + resultado)
else:
    print("Preço Promocional não encontrado")

oferta = site.find("div", class_="ui-pdp-promotions-pill-label", string="OFERTA DO DIA")
if oferta:
    print("ATENÇÃO: Oferta do dia!")
else:
    print("")

link = "https://www.mercadolivre.com.br/climatizador-portatil-frio-joape-bob-preto-220v/p/MLB15468600#polycard_client=recommendations_home_navigation-trend-recommendations&reco_backend=machinalis-homes-pdp-boos&reco_client=home_navigation-trend-recommendations&reco_item_pos=1&reco_backend_type=function&reco_id=25ad0745-0924-4e6d-bb82-e5705c8d4770&wid=MLB2711284948&sid=recos&c_id=/home/navigation-trend-recommendations/element&c_uid=1fa9ec06-034f-4d6a-b821-487bf376995e"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"}

requisicao = requests.get(link, headers=headers)
print(requisicao)

site = BeautifulSoup(requisicao.text, "html.parser")

# Procurando pela tag img com o atributo data-zoom
img = site.find("img", {'data-zoom': True})

# Obtendo a URL da imagem
if img:
    imagem_url = img['data-zoom']

    # Especificando o caminho da pasta onde a imagem será salva
    pasta_destino = "img/"

    # Baixando a imagem
    response = requests.get(imagem_url)

    # Verificando se a requisição foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        filename = imagem_url.split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f'Imagem baixada com sucesso: {filename}')
    else:
        print(f'Falha ao baixar a imagem. Código de status: {response.status_code}')
else:
    print("Imagem não encontrada.")
