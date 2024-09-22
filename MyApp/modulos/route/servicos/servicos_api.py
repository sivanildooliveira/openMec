from MyApp import app
from flask import jsonify
import requests
from bs4 import BeautifulSoup
from MyApp.models import *
from sqlalchemy import or_

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
            return dd
        else:
            return {'status': None}

    else:
        return {'status': None}


@app.route('/api/list_veiculo/<term>', methods=['GET'])
def listVeiculo(term):
    try:
        clientes_com_veiculos = Cliente.query.join(Cliente.veiculos).filter(
            or_(
                Cliente.nome_cliente.like(f'%{term}%'),
                Cliente.telefone.like(f'%{term}%'),
                Cliente.celular.like(f'%{term}%'),
                Cliente.email.like(f'%{term}%'),
                Cliente.cpf.like(f'%{term}%'),
                Veiculo.placa.like(f'%{term}%'),
                Veiculo.fabricante.like(f'%{term}%'),
                Veiculo.modelo.like(f'%{term}%'),
                Veiculo.ano.like(f'%{term}%'),
                Veiculo.cor.like(f'%{term}%'),
                Veiculo.chassi.like(f'%{term}%'),
                Veiculo.motor.like(f'%{term}%'),
                Veiculo.combustivel.like(f'%{term}%'),
                Veiculo.uf.like(f'%{term}%'),
                Veiculo.municipio.like(f'%{term}%')
            )
        ).all()

        
        # Cria uma lista para armazenar os veículos que correspondem ao termo de busca
        veiculos_encontrados = []

        for cliente in clientes_com_veiculos:
            for veiculo in cliente.veiculos:
                # Adiciona o veículo à lista de resultados se encontrar uma correspondência
                veiculos_encontrados.append({
                    'cliente': {
                        'id': cliente.id,
                        'nome_cliente': cliente.nome_cliente,
                        'telefone': cliente.telefone,
                        'celular': cliente.celular,
                        'email': cliente.email,
                        'cpf': cliente.cpf,
                        'cep': cliente.cep,
                        'estado': cliente.estado,
                        'cidade': cliente.cidade,
                        'bairro': cliente.bairro,
                        'rua': cliente.rua,
                        'numero': cliente.numero,
                        'complemento': cliente.complemento,
                    },
                    'veiculo': {
                        'id':veiculo.id,
                        'placa':veiculo.placa,
                        'fabricante':veiculo.fabricante,
                        'modelo':veiculo.modelo,
                        'ano':veiculo.ano,
                        'anomodelo':veiculo.anomodelo,
                        'cor':veiculo.cor,
                        'importado':veiculo.importado,
                        'chassi':veiculo.chassi,
                        'motor':veiculo.motor,
                        'potencia':veiculo.potencia,
                        'cilindrada':veiculo.cilindrada,
                        'combustivel':veiculo.combustivel,
                        'passageiros':veiculo.passageiros,
                        'uf':veiculo.uf,
                        'municipio':veiculo.municipio,
                        'variacaoplacas':veiculo.variacaoplacas,
                    }
                })
        return jsonify(veiculos_encontrados)
    except:
        return jsonify([])


@app.route('/api/list_cliente/<term>', methods=['GET'])
def listCliente(term):
    # Busca os clientes que correspondem ao termo de busca
    
    try:
        clientes_encontrados = Cliente.query.filter(
            or_(
                Cliente.nome_cliente.like(f'%{term}%'),
                Cliente.telefone.like(f'%{term}%'),
                Cliente.celular.like(f'%{term}%'),
                Cliente.email.like(f'%{term}%'),
                Cliente.cpf.like(f'%{term}%'),
                Cliente.cep.like(f'%{term}%'),
                Cliente.estado.like(f'%{term}%'),
                Cliente.cidade.like(f'%{term}%'),
                Cliente.bairro.like(f'%{term}%'),
                Cliente.rua.like(f'%{term}%'),
                Cliente.numero.like(f'%{term}%'),
                Cliente.complemento.like(f'%{term}%'),
            )
        ).all()

    
        resultado_clientes = []

        for cliente in clientes_encontrados:
            # Adiciona o cliente à lista de resultados
            resultado_clientes.append({
                'id': cliente.id,
                'nome': cliente.nome_cliente,
                'telefone': cliente.telefone,
                'celular': cliente.celular,
                'email': cliente.email,
                'cpf': cliente.cpf,
                'cep': cliente.cep,
                'estado': cliente.estado,
                'cidade': cliente.cidade,
                'bairro': cliente.bairro,
                'rua': cliente.rua,
                'numero': cliente.numero,
                'complemento': cliente.complemento,
            })
        
        return jsonify(resultado_clientes)
    except:
        return jsonify([])
