

from MyApp import app, database, filtros
from flask import jsonify, request
import json
import requests
from bs4 import BeautifulSoup
from MyApp.models import *
from sqlalchemy import or_



@app.route('/api/return_dados_veiculo/<placa>', methods=["GET"])
def returDataVeiculo(placa):

    # URL da página que você quer acessar
    url = f'https://www.keplaca.com/placa?placa-fipe=nvs5d69#google_vignette'

    # Fazendo uma requisição GET para a página
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, ilike Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    response = requests.get(url)
    print(response)
 
    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Analisando o conteúdo HTML da página
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Exemplo de como pegar um elemento específico pelo ID
        elemento = soup.find(class_='fipeTablePriceDetail')  # Substitua 'meuID' pelo ID que deseja buscar
        dd = dict()
        print(dd)
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
        print("erros")
        return {'status': None}

@app.route('/api/list_veiculo/<term>', methods=['GET'])
def listVeiculo(term):
    try:
        clientes_com_veiculos = Cliente.query.join(Cliente.veiculos).filter(
            or_(
                Cliente.nome_cliente.ilike(f'%{term}%'),
                Cliente.telefone.ilike(f'%{term}%'),
                Cliente.celular.ilike(f'%{term}%'),
                Cliente.email.ilike(f'%{term}%'),
                Cliente.cpf.ilike(f'%{term}%'),
                Veiculo.placa.ilike(f'%{term}%'),
                Veiculo.fabricante.ilike(f'%{term}%'),
                Veiculo.modelo.ilike(f'%{term}%'),
                Veiculo.ano.ilike(f'%{term}%'),
                Veiculo.cor.ilike(f'%{term}%'),
                Veiculo.chassi.ilike(f'%{term}%'),
                Veiculo.motor.ilike(f'%{term}%'),
                Veiculo.combustivel.ilike(f'%{term}%'),
                Veiculo.uf.ilike(f'%{term}%'),
                Veiculo.municipio.ilike(f'%{term}%')
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

@app.route('/api/buscar_servicos/<term>&<filtro>', methods=['GET'])
def BuscarServicos(term, filtro):
    servicos = []
    
    if filtro == 'all':
        Servicos = database.session.query(Servico).join(Cliente).join(Veiculo, isouter=True).filter(
            or_(
                Cliente.nome_cliente.ilike(f'%{term}%'),
                Cliente.telefone.ilike(f'%{term}%'),
                Cliente.celular.ilike(f'%{term}%'),
                Cliente.email.ilike(f'%{term}%'),
                Cliente.cpf.ilike(f'%{term}%'),
                Cliente.cep.ilike(f'%{term}%'),
                Cliente.estado.ilike(f'%{term}%'),
                Cliente.cidade.ilike(f'%{term}%'),
                Cliente.bairro.ilike(f'%{term}%'),
                Cliente.rua.ilike(f'%{term}%'),
                Cliente.numero.ilike(f'%{term}%'),
                Cliente.complemento.ilike(f'%{term}%'),

                Veiculo.placa.ilike(f'%{term}%'),
                Veiculo.fabricante.ilike(f'%{term}%'),
                Veiculo.modelo.ilike(f'%{term}%'),
                Veiculo.ano.ilike(f'%{term}%'),
                Veiculo.anomodelo.ilike(f'%{term}%'),
                Veiculo.cor.ilike(f'%{term}%'),
                Veiculo.importado.ilike(f'%{term}%'),
                Veiculo.chassi.ilike(f'%{term}%'),
                Veiculo.motor.ilike(f'%{term}%'),
                Veiculo.potencia.ilike(f'%{term}%'),
                Veiculo.cilindrada.ilike(f'%{term}%'),
                Veiculo.combustivel.ilike(f'%{term}%'),
                Veiculo.passageiros.ilike(f'%{term}%'),
                Veiculo.uf.ilike(f'%{term}%'),
                Veiculo.municipio.ilike(f'%{term}%'),
            )
        ).all()
        
        servicos = [serv.to_dict() for serv in Servicos]

    else:
        filtro_cliente = getattr(Cliente, filtro, None)
        filtro_veiculo = getattr(Veiculo, filtro, None)
        filtro_servico = getattr(Servico, filtro, None)
        
        if filtro_cliente:
            n = Cliente.query.filter(filtro_cliente.ilike(f'%{term}%')).all()
            for cli in n:
                for serv in cli.servicos:
                    servicos.append(serv.to_dict())
        
        elif filtro_veiculo:
            n = Cliente.query.filter(filtro_veiculo.ilike(f'%{term}%')).all()
            for vei in n:
                for serv in vei.servicos:
                    servicos.append(serv.to_dict())
        
        else:
            n = Servico.query.filter(filtro_servico.ilike(f'%{term}%')).all()
            for serv in n:
                servicos.append(serv.to_dict())
    
    print(servicos)
                
    return jsonify(servicos)
    
@app.route('/api/list_cliente/<term>', methods=['GET'])
def listCliente(term):

    # Busca os clientes que correspondem ao termo de busca
    
    try:
        clientes_encontrados = Cliente.query.filter(
            or_(
                Cliente.nome_cliente.ilike(f'%{term}%'),
                Cliente.telefone.ilike(f'%{term}%'),
                Cliente.celular.ilike(f'%{term}%'),
                Cliente.email.ilike(f'%{term}%'),
                Cliente.cpf.ilike(f'%{term}%'),
                Cliente.cep.ilike(f'%{term}%'),
                Cliente.estado.ilike(f'%{term}%'),
                Cliente.cidade.ilike(f'%{term}%'),
                Cliente.bairro.ilike(f'%{term}%'),
                Cliente.rua.ilike(f'%{term}%'),
                Cliente.numero.ilike(f'%{term}%'),
                Cliente.complemento.ilike(f'%{term}%'),
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

@app.route('/servicos/api/attserv', methods=['POST'])
def att_serv():
    data = request.get_json()

    return json.dumps({})

@app.route('/servicos/api/status', methods=['POST'])
def att_status():

    data = request.get_json()

    serv = Servico.query.filter_by(id=data['id']).first()
    if serv:
        serv.status = int(data['status'])
        database.session.commit()
        data = {'status': 'ok'}
        return data

    return {'status': 'Serviço não encontrado!'}