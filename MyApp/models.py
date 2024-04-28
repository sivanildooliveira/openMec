from MyApp import app, database
from sqlalchemy import Column,Integer, String, DateTime, Float, ForeignKey
from datetime import datetime
import pytz

class Servico(database.Model):
    id = Column(Integer, primary_key=True)
    os = Column(Integer, nullable=False)
    status = Column(Integer, nullable=False)
    placa = Column(String)
    cliente = Column(String)
    fabricante = Column(String)
    modelo = Column(String)
    ano = Column(String)
    cor = Column(String)
    d_entrada = Column(DateTime, default=datetime.utcnow)
    d_autorizacao = Column(DateTime)
    d_finalizacao = Column(DateTime)
    d_retirada = Column(DateTime)
    
    status = database.Column(database.Integer, nullable=False)
    servicos = database.relationship('MaoDeObra', backref='os', lazy=True)

    def data_formatada(self):
        try:
            data_hora_utc = self.d_entrada
            fuso = pytz.timezone('America/Sao_Paulo')
            data_hora = data_hora_utc.replace(tzinfo=pytz.utc).astimezone(fuso)
        
            return data_hora.strftime('%d/%m/%y %H:%M')
        except:
            pass

class MaoDeObra(database.Model):
    id = Column(Integer, primary_key=True)
    servico = Column(Integer, ForeignKey('servico.id'))
    descricao = Column(String, nullable=False)
    valor = Column(Float, default=0.0)
    desconto = Column(Float, default=0.0)
    responsavel = Column(String)
    porcent_comissao = Column(Float, default=0.0)

    pecas = database.relationship('Pecas', backref='servico', lazy=True)


with app.app_context():
    database.create_all()

