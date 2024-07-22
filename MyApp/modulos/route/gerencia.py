from flask import render_template, url_for, request
from MyApp import app, database, informacoes
from MyApp.modulos.database.servisos_models import Servico, Maodeobra, Peca
from MyApp.defs_aux import *
import json


@app.route('/gerencia')
def gerencia_visao():
    informacoes['modulo'] = 'gerencia'
    informacoes['menu'] = 'visao'

    lista = Servico.query.all()

    print(informacoes)

    return render_template('modulos/gerencia/visao.html', informacoes=informacoes, lista=lista)

