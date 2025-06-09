from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_babel import lazy_gettext as _l

class LeadForm(FlaskForm):
    name = StringField(_l('Nome'), validators=[DataRequired(), Length(max=80)])
    email = StringField(_l('E-mail'), validators=[DataRequired(), Email(), Length(max=120)])
    phone = StringField('Telefone')
    message = TextAreaField(_l('Mensagem'), validators=[Length(max=500)])
    submit = SubmitField(_l('Enviar'))
