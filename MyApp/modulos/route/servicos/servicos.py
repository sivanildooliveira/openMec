from flask import render_template, url_for, request, redirect
from MyApp import app, database, informacoes
from MyApp.models import *
from MyApp.form import FormOs
from MyApp.defs_aux import *
import json
from random import randint


@app.route('/')
def servicos_visao():
    informacoes['modulo'] = 'servicos'
    informacoes['menu'] = 'visao'

    lista = Servico.query.all()
    return render_template('modulos/servicos/visao.html', informacoes=informacoes, lista=lista)


@app.route('/servicos/novidades')
def servicos_novidades():
    informacoes['menu'] = 'novidades'
    lista = Servico.query.all()

    return render_template('modulos/servicos/novidades.html', informacoes=informacoes, lista=lista)


@app.route('/servicos/buscar', methods=['GET', 'POST'])
def servicos_buscar():
    informacoes['menu'] = 'buscar'
    servicos = Servico.query.all()
    
    termo = ''
    filtro = 'all'
    if request.method == 'POST':
        termo = request.form.get('inputBuscar')
        filtro = request.form.get('filter')

    data = []
    sep = []
    cont = 0
    for s in servicos:
        add = False
        for k, very in s.__dict__.items():
            if filtro == 'all':
                add = True
            else:
                if k == filtro:
                    try:
                        if termo.upper() in very.upper():
                            
                            
                            break
                    except:
                        pass
            print(add)
        if add:
            if cont >= 10:
                cont = 0
                sep.append(s)
                data.append(sep)
                sep = []
            else:
                sep.append(s)
                cont += 1
        data.append(sep)

        
    return render_template('modulos/servicos/buscar.html', informacoes=informacoes, servicos=data, termo=termo, filtro=filtro)


@app.route('/servicos/<id>')
def servico_visualizar(id):
    global informacoes
    informacoes['menu'] = 'visualizar'
    if id != 'idserv':
        informacoes['id_os'] = id
    else:
        id = informacoes['id_os']

    servico = Servico.query.filter_by(id=id).first()
    
    return render_template('modulos/servicos/servico_visualizar.html', informacoes=informacoes, serv=servico)


@app.route('/servicos/criar', methods=['GET','POST'])
def servicos_criar():

    global informacoes
    informacoes['menu'] = 'criar'
    data_hora = data_formatada()
    form = FormOs()

    if form.validate_on_submit():

        try:
            id_cliente = int(form.id_cliente.data)
        except:
            id_cliente = False

        if id_cliente:
            cliente = Cliente.query.filter_by(id=id_cliente).first()
        else:
            cliente = Cliente(
                                nome_cliente=form.nome_cliente.data if form.nome_cliente.data else '',
                                telefone=form.telefone.data if form.telefone.data else '',
                                celular=form.celular.data if form.celular.data else '',
                                email=form.email.data if form.email.data else '',
                                cpf=form.cpf.data if form.cpf.data else '',
                                cep=form.cep.data if form.cep.data else '',
                                estado=form.estado.data if form.estado.data else '',
                                cidade=form.cidade.data if form.cidade.data else '',
                                bairro=form.bairro.data if form.bairro.data else '',
                                rua=form.rua.data if form.rua.data else '',
                                numero=form.numero.data if form.numero.data else '',
                                complemento=form.complemento.data if form.complemento.data else''
                            )
            
            database.session.add(cliente)
            database.session.commit()

        
        veiculo = Veiculo.query.filter_by(placa=form.placa.data).first()
        if not veiculo:
            veiculo = Veiculo(
                                placa=form.placa.data if form.placa.data else '',
                                fabricante=form.fabricante.data  if form.fabricante.data else '',
                                modelo=form.modelo.data if form.modelo.data else '',
                                ano=form.ano.data  if form.ano.data else '',
                                anomodelo=form.anomodelo.data if form.anomodelo.data else '',
                                cor=form.cor.data  if form.cor.data else '',
                                importado=form.importado.data if form.importado.data else '',
                                chassi=form.chassi.data  if form.chassi.data else '',
                                motor=form.motor.data if form.motor.data else '',
                                potencia=form.potencia.data if form.potencia.data else '',
                                cilindrada=form.cilindrada.data if form.cilindrada.data else '',
                                combustivel=form.combustivel.data  if form.combustivel.data else '',
                                passageiros=form.passageiros.data if form.passageiros.data else '',
                                uf=form.uf.data  if form.uf.data else '',
                                municipio=form.municipio.data if form.municipio.data else '',    
                            )
            
            database.session.add(veiculo)
            database.session.commit()



        if veiculo not in cliente.veiculos:
            cliente.veiculos.append(veiculo)
            database.session.commit()
        
        servico = Servico(os=randint(0,500), id_cliente=cliente.id, id_veiculo=veiculo.id)
        database.session.add(servico)
        database.session.commit()
        
        return redirect(url_for('servico_visualizar', id=servico.id))
        

    return render_template('modulos/servicos/criar.html', informacoes=informacoes, form=form, data_hora=data_hora)


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

