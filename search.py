import requests
from bs4 import BeautifulSoup
from datetime import datetime
# URL da página do artigo
url_continente = "https://www.continente.pt/"
url_elcorteingles = "https://www.elcorteingles.pt/supermercado/"
url_garrafeirasoares = "https://www.garrafeirasoares.pt/pt/"
# products_id = ["5601012011500", "5601012001310", "5601012004427", "5601012011920"]
products_id = {"Mateus Rosé Original": "5601012011500", "Mateus Sparkling": "5601012001310", "Trinca Bolotas Tinto": "5601012004427", "Papa Figos Branco": "5601012011920"}
# Continente
for key, value in products_id.items():
    # connection to the page
    response = requests.get(url_garrafeirasoares + "resultado-da-pesquisa_36.html?term=" + value)
    print(response.url)
    # check if the request was successful
    if response.status_code == 200:
        # parse the HTML of the page
        soup = BeautifulSoup(response.text, "html.parser")
        # find the link to the product page
        link_element = soup.find("a", href=lambda href: href and href.startswith("https://www.continente.pt/produto/"))
        # check if there is content
        if link_element:
            # get the link
            link = link_element.get("href")
            # check if the link was found
            if (link):
                # connection to the product page
                response = requests.get(link)
                # check if the request was successful
                if (response.status_code == 200):
                    soup = BeautifulSoup(response.text, "html.parser")
                    # find the price
                    preco = soup.find("span", class_="ct-price-formatted")
                    # Get the current date and time
                    now = datetime.now()
                    #Format the date and time as a string
                    date_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    # Verificar se o elemento foi encontrado
                    if preco:
                        print(f"Store name: Continente")
                        print(f"Wine name: {key}")
                        print(f"Harvest year: N/A")
                        print(f"Capacity: 75cl")
                        print(f"Discount: TODO")
                        print(f"Price and currency: {preco.text.strip()}")
                        print(f"Date of scraping: {date_string}, WEST timezone")
                        print(f"Location: Portugal // TODO")
                        print(f"Product link: {link}\n")
                    else:
                        print("Não foi possível acessar a página do artigo.\n")
                else:
                    print("Não foi possível acessar a página do artigo.\n")
            else:
                print("Não foi possível acessar a página do artigo.\n")
        else:
            print("Não foi possível acessar a página do artigo.\n")
    else:
        print("Não foi possível acessar a página do artigo.\n")