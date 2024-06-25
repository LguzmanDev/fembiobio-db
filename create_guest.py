# create_guest.py
from app import app, db
from app.models import User

with app.app_context():
    # Crear un usuario invitado
    guest_user = User(username='INVITADO')
    guest_user.set_password('INVITADO')
    guest_user.role = 'guest'
    db.session.add(guest_user)
    db.session.commit()

    print("Usuario invitado creado con éxito.")
