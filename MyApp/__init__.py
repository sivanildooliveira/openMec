from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)
app.secret_key = '29cecf8afd6176f06bb3f55472d490d1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///openmec.db'

database = SQLAlchemy()
database.init_app(app)

migrate = Migrate(app, database)




filtros = 'os-Nª Serviço,nome_cliente-Nome Cliente,telefone-Telefone Cliente,celular-Celular Cliente,email-Email Cliente,cpf-CPF Cliente,cep-CEP Cliente,estado-Estado Cliente,cidade-Cidade Cliente,bairro-Bairro Cliente,rua-Rua Cliente,numero-Numero Cliente,complemento-Complemento Cliente,placa-Placa Veiculo,fabricante-Fabricante Veiculo,modelo-Modelo Veiculo,ano-Ano Fabricação Veiculo,anomodelo-Ano Modelo Veiculo,cor-Cor Veiculo,chassi-Chassi Veiculo,motor-Motor Veiculo,potencia-Potencia Veiculo,cilindrada-Cilindrada Veiculo,combustivel-Combustivel Veiulo,uf-UF Veiculo,municipio-Municipio Veiculo,d_entrada-Data de Entrada,d_autorizacao-Data de Autorização,d_finalizacao-Data de Finalização,d_retirada-Data de Retirada'.split(',')
informacoes = {
    'modulo': None,
    'menu': None,
    'id_os': None,
    'filtros_db': [(key.split('-')[0], key.split('-')[1]) for  key in filtros]
}


from MyApp import route

