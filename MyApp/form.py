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
    placa = StringField('Placa')
    cliente = StringField('Cliente')
    fabricante = StringField('Fabricante')
    modelo = StringField('Modelo')
    ano = StringField('Ano')
    cor = StringField('Cor')

    submit = SubmitField('Salvar')

