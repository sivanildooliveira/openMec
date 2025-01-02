from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)
app.secret_key = '29cecf8afd6176f06bb3f55472d490d1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///openmec.db'

database = SQLAlchemy()
database.init_app(app)

migrate = Migrate(app, database)


filtros = [x.split('-') for x in 'all-Todos os Campos-all,os-Nª Serviço-Cliente,nome_cliente-Nome Cliente-Cliente,telefone-Telefone Cliente-Cliente,celular-Celular Cliente-Cliente,email-Email Cliente-Cliente,cpf-CPF Cliente-Cliente,cep-CEP Cliente-Cliente,estado-Estado Cliente-Cliente,cidade-Cidade Cliente-Cliente,bairro-Bairro Cliente-Cliente,rua-Rua Cliente-Cliente,numero-Numero Cliente-Cliente,complemento-Complemento Cliente-Cliente,placa-Placa Veiculo-Veiculo,fabricante-Fabricante Veiculo-Veiculo,modelo-Modelo Veiculo-Veiculo,ano-Ano Fabricação Veiculo-Veiculo,anomodelo-Ano Modelo Veiculo-Veiculo,cor-Cor Veiculo-Veiculo,chassi-Chassi Veiculo-Veiculo,motor-Motor Veiculo-Veiculo,potencia-Potencia Veiculo-Veiculo,cilindrada-Cilindrada Veiculo-Veiculo,combustivel-Combustivel Veiculo-Veiculo,uf-UF Veiculo-Veiculo,municipio-Municipio Veiculo-Veiculo,d_entrada-Data de Entrada,d_autorizacao-Data de Autorização,d_finalizacao-Data de Finalização,d_retirada-Data de Retirada'.split(',')]

informacoes = {
    'modulo': None,
    'menu': None,
    'id_os': None,
    'filtros_db': filtros
}


from MyApp import route

