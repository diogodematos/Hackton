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
    if response.status_code == 200:
    # Parse the HTML of the page
      soup = BeautifulSoup(response.text, "html.parser")
    # Check if there is a JavaScript redirection
      script = soup.find("script")
      if script:
        # Extract the URL from the JavaScript
        script_text = script.text
        start_index = script_text.find("location='") + len("location='")
        end_index = script_text.find("'", start_index)
        redirect_url = script_text[start_index:end_index]
        # Now, you can send a new request to the redirection URL
        response = requests.get(redirect_url)
        if response.status_code == 200:
            # Parse the content of the redirected page
            soup = BeautifulSoup(response.text, "html.parser")
            # Now you can extract data from the redirected page using 'redirected_soup'
            # print(soup)
            preco = soup.find("span", class_="current").text.strip()
            now = datetime.now()
            date_string = now.strftime("%d/%m/%Y %H:%M:%S")
            
            # Print the extracted information
            print("Store name: Garrafeira Soares")
            print(f"Wine name: {key}")
            print("Harvest year: N/A")
            print("Capacity: 75cl")
            print("Discount: TODO")
            print(f"Price and currency: {preco}")
            print(f"Date of scraping: {date_string}, WEST timezone")
            print("Location: Portugal // TODO")
            print(f"Product link: {redirect_url}\n")
        else:
            print("Failed to access the redirection URL.")
    else:
        print("No JavaScript redirection found on the initial page.")


            