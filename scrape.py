import requests
from bs4 import BeautifulSoup
import csv

# Cria o arquivo CSV para armazenar os dados coletados
csv_file = open('livros_publish_news.csv', 'w', encoding='utf-8', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Título', 'Editora', 'Autor', 'Número de páginas', 'Categoria', 'Vendas'])

# Define a URL base e os parâmetros da pesquisa
base_url = 'https://www.publishnews.com.br/ranking/anual/0'
ano_inicial = 2022
ano_final = 2018

# Loop pelas páginas de cada ano e faz o scraping das informações
for ano in range(ano_inicial, ano_final-1, -1):
    url = f'{base_url}/{ano}/0/0'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Encontra a tabela com os dados dos livros
    table = soup.find('table', class_='best-sellers')

    # Loop pelas linhas da tabela e extrai as informações de cada livro
    for row in table.tbody.find_all('tr'):
        cols = row.find_all('td')

        # Extrai as informações do livro
        titulo = cols[0].find('a').text.strip()
        editora = cols[1].text.strip()
        autor = cols[2].text.strip()
        num_paginas = cols[3].text.strip()
        categoria = cols[4].text.strip()
        vendas = cols[5].text.strip()

        # Escreve as informações do livro no arquivo CSV
        csv_writer.writerow([titulo, editora, autor, num_paginas, categoria, vendas])

# Fecha o arquivo CSV
csv_file.close()
