from flask import render_template, url_for, request
from MyApp import app, database
from MyApp.models import Servico, Maodeobra, Peca
from MyApp.form import FormOs
from MyApp.defs_aux import *
import json






@app.route('/')
def servicos():
    lista = Servico.query.all()

    return render_template('servicos/novidades.html', lista=lista)


@app.route('/servicos/buscar')
def servicos_buscar():

    pecas = Peca.query.all()
    mao_de_obra = Maodeobra.query.all()

    return render_template('servicos/buscar.html')


@app.route('/servicos/<id>')
def servico_visualizar(id):
    servico = Servico.query.filter_by(id=id).first()
    servicos = servico.servicos

    print(servico.status)
    
    return render_template('servicos/servico_visualizar.html', serv=servico)


@app.route('/servicos/criar', methods=['GET','POST'])
def servicos_criar():

    data_hora = data_formatada()
    form = FormOs()

    if form.validate_on_submit():

        os = datetime.now().second
        placa = form.placa.data
        cliente = form.cliente.data
        fabricante = form.fabricante.data
        modelo = form.modelo.data
        ano = form.ano.data
        cor = form.cor.data
        status = 1

        n = Servico(os=os, placa=placa, cliente=cliente, fabricante=fabricante, modelo=modelo, ano=ano, cor=cor, status=status)
        database.session.add(n)
        database.session.commit()

    return render_template('servicos/criar.html', form=form, data_hora=data_hora)


@app.route('/servicos/api/attserv', methods=['POST'])
def att_serv():
    data = request.get_json()

    print(data)

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

