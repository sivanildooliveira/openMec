from MyApp import app, database
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Table
from datetime import datetime
import pytz

# Tabela de Associação para o relacionamento muitos-para-muitos entre Cliente e Veiculo
cliente_veiculo = Table(
    'cliente_veiculo',
    database.Model.metadata,
    Column('cliente_id', Integer, ForeignKey('cliente.id'), primary_key=True),
    Column('veiculo_id', Integer, ForeignKey('veiculo.id'), primary_key=True)
)


class Cliente(database.Model):
    id = Column(Integer, primary_key=True)
    nome_cliente = Column(String, nullable=False)
    telefone = Column(String)
    celular = Column(String, nullable=False)
    email = Column(String)
    cpf = Column(String)
    cep = Column(String)
    estado = Column(String)
    cidade = Column(String)
    bairro = Column(String)
    rua = Column(String)
    numero = Column(String)
    complemento = Column(String)

    servicos = database.relationship('Servico', backref='cliente', lazy=True)
    
    # Relacionamento muitos-para-muitos com Veiculo através da tabela de associação
    veiculos = database.relationship(
        'Veiculo',
        secondary=cliente_veiculo,
        back_populates='clientes'
    )


class Veiculo(database.Model):
    id = Column(Integer, primary_key=True)
    placa = Column(String, nullable=False)
    fabricante = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    ano = Column(String)
    anomodelo = Column(String)
    cor = Column(String)
    importado = Column(String)
    chassi = Column(String)
    motor = Column(String)
    potencia = Column(String)
    cilindrada = Column(String)
    combustivel = Column(String)
    passageiros = Column(String)
    uf = Column(String)
    municipio = Column(String)
    variacaoplacas = Column(String)

    servicos = database.relationship('Servico', backref='veiculo', lazy=True)
    
    # Relacionamento muitos-para-muitos com Cliente através da tabela de associação
    clientes = database.relationship(
        'Cliente',
        secondary=cliente_veiculo,
        back_populates='veiculos'
    )


class Servico(database.Model):
    id = Column(Integer, primary_key=True)
    os = Column(Integer, nullable=False)
    status = Column(Integer, default=0)
    id_cliente = Column(database.Integer, database.ForeignKey('cliente.id'), nullable=False)
    id_veiculo = Column(database.Integer, database.ForeignKey('veiculo.id'), nullable=False)
    d_entrada = Column(DateTime, default=datetime.utcnow)
    d_autorizacao = Column(DateTime)
    d_finalizacao = Column(DateTime)
    d_retirada = Column(DateTime)
    mao_de_obra = database.relationship('Maodeobra', backref='os', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "os": self.os,
            "status": self.status,
            "nome_cliente": self.cliente.nome_cliente,
            "telefone": self.cliente.telefone,
            "celular": self.cliente.celular,
            "email": self.cliente.email,
            "cpf": self.cliente.cpf,
            "placa": self.veiculo.placa,
            "fabricante": self.veiculo.fabricante,
            "modelo": self.veiculo.modelo,
            "ano": self.veiculo.ano,
            "cor": self.veiculo.cor,
            "chassi": self.veiculo.chassi,
            "potencia": self.veiculo.potencia,
            "cilindrada": self.veiculo.cilindrada,
            "total": self.retur_total()
        }

    def retur_total(self):
        tot = 0
        return f'R$ {tot:.2f}'
    
    def return_data_hora(self, status):
        try:
            if status == 1:
                data = self.d_entrada
            elif status == 2:
                data = self.d_autorizacao
            elif status == 3:
                data = self.d_finalizacao
            elif status == 4:
                data = self.d_retirada
            return str(datetime.strftime(data, '%Y-%m-%dT%H:%M'))
        except:
            return None
    
    def data_formatada(self):
        try:
            data_hora_utc = self.d_entrada
            fuso = pytz.timezone('America/Sao_Paulo')
            data_hora = data_hora_utc.replace(tzinfo=pytz.utc).astimezone(fuso)
            return data_hora.strftime('%d/%m/%y %H:%M')
        except:
            pass


class Maodeobra(database.Model):
    id = Column(Integer, primary_key=True)
    servico_id = Column(Integer, ForeignKey('servico.id'))
    descricao = Column(String, nullable=False)
    valor = Column(Float, default=0.0)
    desconto = Column(Float, default=0.0)
    responsavel = Column(String)
    porcent_comissao = Column(Float, default=0.0)
    pecas = database.relationship('Peca', backref='serv', lazy=True)


class Peca(database.Model):
    id = Column(Integer, primary_key=True)
    mao_de_obra_id = Column(Integer, ForeignKey('maodeobra.id'))
    descricao = Column(String, nullable=False)
    valor = Column(Float, default=0.0)
    qtd = Column(Float, default=0.0)
    desconto = Column(Float, default=0.0)


with app.app_context():
    database.create_all()
