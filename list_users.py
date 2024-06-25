from app import app, db
from app.models import User

with app.app_context():
    # Consulta todos los usuarios en la base de datos
    users = User.query.all()

    # Comprueba si hay usuarios en la base de datos
    if not users:
        print("No hay usuarios en la base de datos.")
    else:
        # Imprime los nombres de usuario y sus roles
        for user in users:
            print(f"Username: {user.username}, Role: {user.role}")
