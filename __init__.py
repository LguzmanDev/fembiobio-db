from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sduhhljs:JB7TXM8R7Rsb5To8b2ZodPJ_H7CjAfEv@silly.db.elephantsql.com/sduhhljs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '@FEMBIOBIO2024'  # Cambia esto por una clave real en producción
app.config['DEBUG'] = True  # Habilitar el modo de depuración

csrf = CSRFProtect(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
bcrypt = Bcrypt(app)

from app import routes, models  # Importa las rutas y modelos después de inicializar `app` y `db`

@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))
