import requests

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
buscar_empresa_por_cnpj(cnpj)