from flask import render_template, url_for, request
from MyApp import app, database, informacoes
from MyApp.models import *
from MyApp.defs_aux import *


@app.route('/gerencia')
def gerencia_visao():
    informacoes['modulo'] = 'gerencia'
    informacoes['menu'] = 'visao'

    lista = Servico.query.all()

    print(informacoes)

    return render_template('modulos/gerencia/visao.html', informacoes=informacoes, lista=lista)

