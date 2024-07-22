from MyApp import app, database


from MyApp.modulos.database import servisos_models

with app.app_context():
    database.create_all()

