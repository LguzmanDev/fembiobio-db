from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User


class DeleteForm(FlaskForm):
    submit = SubmitField('Eliminar')



class EmprendimientoForm(FlaskForm):
    run = StringField('RUN', validators=[DataRequired()])
    rut = StringField('RUT')
    nombre_emprendimiento = StringField('Nombre del Emprendimiento', validators=[DataRequired()])
    razon_social = StringField('Razón Social')
    nombre_representante = StringField('Nombre del Representante', validators=[DataRequired()])
    correo_electronico = StringField('Correo Electrónico', validators=[DataRequired(), Email()])
    telefono = StringField('Teléfono')
    direccion = StringField('Dirección')
    provincia = StringField('Provincia')
    comuna = StringField('Comuna')
    estado = SelectField('Estado', choices=[('si', 'Sí'), ('no', 'No'), ('error', 'Error')], validators=[DataRequired()])
    logo = StringField('Logo')
    video = StringField('Video')
    redes_sociales = TextAreaField('Redes Sociales')
    resena = TextAreaField('Reseña')
    productos = TextAreaField('Productos')
    notas = TextAreaField('Notas')  # Nuevo campo
    submit = SubmitField('Guardar')



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')