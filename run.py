from app import app, db

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea las tablas, ahora dentro del contexto de la aplicación
    app.run(debug=True)

