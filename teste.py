import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# EAN do vinho Mateus Rose
ean = "5601012011500"

# Caminho para o executável do ChromeDriver
chrome_driver_path = '/usr/bin/chromedriver'

# Configurar o serviço do ChromeDriver
service = Service(executable_path=chrome_driver_path)

# Inicializar o driver do navegador Chrome
driver = webdriver.Chrome(service=service)


# Abra a página da Garrafeira Soares
driver.get("https://www.garrafeirasoares.pt/")

# Aguarde um pouco para que a página seja carregada completamente (ajuste o tempo conforme necessário)
time.sleep(5)

# Localize o botão de confirmação de idade e clique nele
confirm_button = driver.find_element(By.XPATH, '//a[@class="button"]')
confirm_button.click()

# Aguarde um pouco após clicar no botão (ajuste o tempo conforme necessário)
time.sleep(3)

# Realize uma pesquisa usando o EAN
search_box = driver.find_element(By.ID, "search-box")
search_box.send_keys(ean)
search_box.send_keys(Keys.RETURN)

# Aguarde um pouco para que a página de resultados seja carregada (ajuste o tempo conforme necessário)
time.sleep(5)

# Extraia as informações do vinho da página de resultados
result = driver.find_element(By.CLASS_NAME, "product-card")

# Nome do vinho
nome = result.find_element(By.CLASS_NAME, "product-name").text

# Preço do vinho
preco = result.find_element(By.CLASS_NAME, "product-price").text

# Imprima as informações
print(f"Nome: {nome}")
print(f"Preço: {preco}")

# Feche o navegador
driver.quit()
