from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, IntegerField, BooleanField, FloatField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError




class FormCliente(FlaskForm):
	id = StringField('id:')
	nome = StringField('Nome: ', render_kw={"autocomplete":"off", "oninput": "upercase(this)"}, validators=[DataRequired()])
	telefone = StringField('Telefone: ', render_kw={"placeholder":"(xx) x xxxx-xxxx", "inputmode":"numeric", "oninput":"inputTelefone(this)", "autocomplete":"off"})
	celular = StringField('Celular: ', render_kw={"placeholder":"(xx) x xxxx-xxxx", "inputmode":"numeric", "oninput":"inputTelefone(this)", "autocomplete":"off"})
	documento = StringField('CPF/CNPJ: ', render_kw={"placeholder":"___.___.___-__" ,"inputmode":"numeric" , "oninput": "inputCpfCnpj(this)", "autocomplete":"off"})
	estado = StringField('Estado: ', render_kw={"autocomplete":"off", "oninput": "upercase(this)"})
	cidade = StringField('Cidade: ', render_kw={"autocomplete":"off", "oninput": "upercase(this)"})
	bairro = StringField('Bairro: ', render_kw={"autocomplete":"off", "oninput": "upercase(this)"})
	logradouro = StringField('Logradouro: ', render_kw={"autocomplete":"off", "oninput": "upercase(this)"})
	numero = StringField('Numero: ', render_kw={"autocomplete":"off", "oninput": "upercase(this)"})
	complemento = StringField('Complemento: ', render_kw={"autocomplete":"off", "oninput": "upercase(this)"})
	submit_cliente = SubmitField('salvar')


class FormOs(FlaskForm):
    
    id_cliente = StringField()

    placa = StringField('Placa', validators=[DataRequired()])
    fabricante = StringField('Fabricante', validators=[DataRequired()])
    modelo = StringField('Modelo', validators=[DataRequired()])
    ano = StringField('Ano')
    anomodelo = StringField('Ano Modelo')
    cilindrada = StringField('Cilindrada')
    potencia = StringField('Potencia')
    combustivel = StringField('Combustivel')
    chassi = StringField('Chassi')
    motor = StringField('Motor')
    passageiros = IntegerField('Passageiros')
    uf = StringField('UF')
    municipio = StringField('Município')
    valorvenal = StringField('Valor Venal')
    importado = StringField('Importado')
    cor = StringField('Cor')

    nome_cliente = StringField('Nome do Cliente', validators=[DataRequired()])
    telefone = StringField('Telefone')
    celular = StringField('Celular', validators=[DataRequired()])
    email = StringField('Email')
    cpf = StringField('CPF')
    cep = StringField('CEP')
    estado = StringField('Estado')
    cidade = StringField('Cidade')
    bairro = StringField('Bairro')
    rua = StringField('Rua')
    numero = StringField('Número')
    complemento = StringField('Complemento')
    submit = SubmitField('Salvar')

