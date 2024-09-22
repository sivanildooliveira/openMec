import requests
from bs4 import BeautifulSoup

def buscar_empresa_por_cnpj(cnpj):
    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        if 'status' in dados and dados['status'] == 'ERROR':
            print(f"Erro: {dados['message']}")
        else:
            print(f"Nome: {dados['nome']}")
            print(f"Fantasia: {dados['fantasia']}")
            print(f"Situação: {dados['situacao']}")
            print(f"Logradouro: {dados['logradouro']}")
            print(f"Complemento: {dados['complemento']}")
            print(f"Bairro: {dados['bairro']}")
            print(f"Município: {dados['municipio']}")
            print(f"UF: {dados['uf']}")
            print(f"CEP: {dados['cep']}")
            print(f"Telefone: {dados['telefone']}")
            print(f"Email: {dados['email']}")
        print(dados)
    else:
        print("Erro ao acessar a API.")

# Exemplo de uso
cnpj = "04877032193"  # Substitua por um CNPJ válido
#buscar_empresa_por_cnpj(cnpj)


def returDataVeiculo(placa):

    # URL da página que você quer acessar
    url = f'https://www.keplaca.com/placa?placa-fipe={placa}'

    # Fazendo uma requisição GET para a página
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    print(response)
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

n = int('35')
print(n)
