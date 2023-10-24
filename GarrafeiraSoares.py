import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# EAN do vinho Mateus Rose
products_id = {"Mateus Rosé Original": "5601012011500", "Mateus Sparkling": "5601012001310", "Trinca Bolotas Tinto": "5601012004427", "Papa Figos Branco": "5601012011920"}

for key, value in products_id.items():

# Inicialize o driver do navegador (você precisa ter o WebDriver correspondente instalado)
	driver = webdriver.Chrome()

	# Abra a página da Garrafeira Soares
	driver.get("https://www.garrafeirasoares.pt/")

	# Aguarde um pouco para que a página seja carregada completamente (ajuste o tempo conforme necessário)


	# Localize o botão de confirmação de idade e clique nele
	confirm_button = driver.find_element(By.XPATH, '//a[@class="button" and @href="javascript:void(0);"]')
	confirm_button.click()

	# Aguarde um pouco após clicar no botão (ajuste o tempo conforme necessário)
	time.sleep(1)

	# Realize uma pesquisa usando o EAN
	search_box = driver.find_element(By.ID, "search")
	search_box.send_keys(value)
	search_box.send_keys(Keys.RETURN)

	# Aguarde um pouco para que a página de resultados seja carregada (ajuste o tempo conforme necessário)
	time.sleep(1)

	# Aguarde até que o botão de fechar (confirm_button) esteja visível
	#

	# Extraia as informações do vinho da página de resultados
	result = driver.find_element(By.CLASS_NAME, "product-info")

	# Nome do vinho
	div_element = driver.find_element(By.CLASS_NAME, "name")

	nome = div_element.find_element(By.TAG_NAME, "h1").text

	capacidade_element = driver.find_element(By.XPATH, '//p[@class="title" and contains(text(), "Capacidade")]')

	# Em seguida, localize o próximo elemento <p> (o que contém o valor da capacidade)
	capacidade = capacidade_element.find_element(By.XPATH, './following-sibling::p').text

	local_element = driver.find_element(By.XPATH, '//p[@class="title" and contains(text(), "Região")]')
	local = local_element.find_element(By.XPATH, './following-sibling::p').text


	# Preço do vinho
	preco = driver.find_element(By.CLASS_NAME, "current").text

	# Imprima as informações
	if result:
		print(f"Store name: Garrafeira Soares")
		print(f"Wine name: {nome}")
		print(f"Harvest year: N/A")
		print(f"Capacity: {capacidade}")
		print(f"Discount: TODO")
		print(f"Price and currency: {preco}")
		#print(f"Date of scraping: {date_string}, WEST timezone")
		print(f"Location: {local} // TODO")
		#print(f"Product link: {link}\n")
		print(f"Preço: {preco}")

# Feche o navegador
driver.quit()
