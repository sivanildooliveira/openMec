from MyApp import app
import requests
import json
from bs4 import BeautifulSoup

@app.route('/api/return_dados_veiculo/<placa>', methods=["GET"])
def returDataVeiculo(placa):

    # URL da página que você quer acessar
    url = f'https://www.keplaca.com/placa?placa-fipe={placa}'

    # Fazendo uma requisição GET para a página
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Analisando o conteúdo HTML da página
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Exemplo de como pegar um elemento específico pelo ID
        elemento = soup.find(class_='fipeTablePriceDetail')  # Substitua 'meuID' pelo ID que deseja buscar
        dd = dict()
        if elemento:
            for c in elemento:
                dd[c.find('b').text[:-1].replace(' ', '')] = c.find_all('td')[1].text
            try:
                dd["Valor Venal"] = soup.find_all(class_='tableNumber')[0].text
            except:
                dd["Valor Venal"] = ''
            try:
                dd["VariacaoPlacas"] = [a.text.split(' ')[1] for a in soup.find_all('figcaption')]
            except:
                dd["VariacaoPlacas"] = ''
            print(dd)
            return dd
        else:
            return {'status': None}

    else:
        return {'status': None}
