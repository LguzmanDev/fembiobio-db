from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(64), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @property
    def is_active(self):
        # Aquí puedes agregar lógica para desactivar usuarios si es necesario
        return True

    def get_id(self):
        return str(self.id)

# Debes asegurarte de tener el método is_active en la clase User para que funcione con Flask-Login)


class Emprendimiento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    run = db.Column(db.String(12), nullable=False)
    rut = db.Column(db.String(12))
    nombre_emprendimiento = db.Column(db.String(200), nullable=False)
    razon_social = db.Column(db.String(200))
    nombre_representante = db.Column(db.String(200), nullable=False)
    correo_electronico = db.Column(db.String(200), nullable=False)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(200))
    provincia = db.Column(db.String(200))
    comuna = db.Column(db.String(200))
    estado = db.Column(db.String(20))
    detalles = db.relationship('Detalle', backref='emprendimiento', uselist=False, cascade="all, delete-orphan")

class Detalle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emprendimiento_id = db.Column(db.Integer, db.ForeignKey('emprendimiento.id'), nullable=False)
    logo = db.Column(db.String(200))
    video = db.Column(db.String(200))
    redes_sociales = db.Column(db.String(200))
    resena = db.Column(db.Text)
    productos = db.Column(db.Text)
    notas = db.Column(db.Text, nullable=True)  