import requests
from bs4 import BeautifulSoup
from datetime import datetime
# URL da página do artigo
url_garrafeirasoares = "https://www.garrafeirasoares.pt/pt/"
products_id = {"Mateus Rosé Original": "5601012011500", "Mateus Sparkling": "5601012001310", "Trinca Bolotas Tinto": "5601012004427", "Papa Figos Branco": "5601012011920", "Porto Graham's": "5010867410329"}
# Continente
# Função para extrair informações de uma página
def extract_product_info(url, product_name):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Verifique se há uma redireção JavaScript
        script = soup.find("script")
        if script:
            script_text = script.text
            start_index = script_text.find("location='") + len("location='")
            end_index = script_text.find("'", start_index)
            redirect_url = script_text[start_index:end_index]

            response = requests.get(redirect_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")

                # Extraia informações da composição do produto
                product_composition = soup.find("div", class_="product-composition")

                product_info = {}
                rows = product_composition.find_all("div", class_="row")

                for row in rows:
                    column_head = row.find("div", class_="col-sm-4 column column-head").text.strip()
                    column_info = row.find("div", class_="col-sm-8 column column-info").text.strip()
                    product_info[column_head] = column_info

                # Obtenha o preço
                preco = soup.find("span", class_="current").text.strip()
                discount = soup.find("span", class_="discount")
                if discount:
                    discount = discount.text.lstrip('-').strip()
                else:
                    discount = "N/A"


                # Obtenha a hora atual com o fuso horário 'WEST'
                now = datetime.now()
                date_string = now.strftime("%d/%m/%Y %H:%M:%S %Z")

                # Imprima as informações extraídas
                print("Store name: Garrafeira Soares")
                print(f"Wine name: {product_name}")
                print(f"Harvest year: {product_info.get('Colheita', 'N/A')}")
                print(f"Capacity: {product_info.get('Capacidade', 'N/A')}")
                print(f"Discount: {discount}")
                print(f"Price and currency: {preco}")
                print(f"Date of scraping: {date_string}")
                print("Local: Online Store")
                print(f"Product link: {redirect_url}\n")
            else:
                print("Failed to access the redirection URL.")
        else:
            print("No JavaScript redirection found on the initial page.")
    else:
        print(f"Failed to access the page for product: {product_name}")

# Processa os produtos
for product_name, product_id in products_id.items():
    product_url = url_garrafeirasoares + f"resultado-da-pesquisa_36.html?term={product_id}"
    extract_product_info(product_url, product_name)


            