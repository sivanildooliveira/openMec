from flask import render_template, url_for, request
from MyApp import app, database, informacoes
from MyApp.modulos.database.servisos_models import Servico, Maodeobra, Peca
from MyApp.form import FormOs
from MyApp.defs_aux import *
import json


@app.route('/')
def servicos_visao():
    informacoes['modulo'] = 'servicos'
    informacoes['menu'] = 'visao'

    lista = Servico.query.all()
    print(informacoes)
    return render_template('modulos/servicos/visao.html', informacoes=informacoes, lista=lista)



@app.route('/servicos/novidades')
def servicos_novidades():
    global informacoes
    informacoes['menu'] = 'novidades'

    lista = Servico.query.all()

    return render_template('modulos/servicos/novidades.html', informacoes=informacoes, lista=lista)


@app.route('/servicos/buscar')
def servicos_buscar():
    global informacoes
    informacoes['menu'] = 'buscar'

    pecas = Peca.query.all()
    mao_de_obra = Maodeobra.query.all()

    return render_template('modulos/servicos/buscar.html', informacoes=informacoes)


@app.route('/servicos/<id>')
def servico_visualizar(id):
    global informacoes
    informacoes['menu'] = 'visualizar'
    if id != 'idserv':
        informacoes['id_os'] = id
    else:
        id = informacoes['id_os']

    servico = Servico.query.filter_by(id=id).first()
    servicos = servico.servicos
    print(servico.status)
    
    return render_template('modulos/servicos/servico_visualizar.html', informacoes=informacoes, serv=servico)


@app.route('/servicos/criar', methods=['GET','POST'])
def servicos_criar():
    global informacoes
    informacoes['menu'] = 'criar'

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

    return render_template('modulos/servicos/criar.html', informacoes=informacoes, form=form, data_hora=data_hora)


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

