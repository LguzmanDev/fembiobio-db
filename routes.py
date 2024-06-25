from flask import render_template, request, redirect, url_for, flash
from app import app, db, bcrypt
from app.models import Emprendimiento, Detalle, User
from app.forms import EmprendimientoForm, DeleteForm, LoginForm, RegistrationForm
from flask_login import login_user, logout_user, login_required, current_user
from functools import wraps
from flask import abort
from flask_login import current_user

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

def role_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated or current_user.role != role:
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator

@app.route('/')
@login_required
def index():
    emprendimientos = Emprendimiento.query.all()
    count_si = Emprendimiento.query.filter_by(estado='si').count()
    count_no = Emprendimiento.query.filter_by(estado='no').count()
    count_error = Emprendimiento.query.filter_by(estado='error').count()
    count_total = len(emprendimientos)
    delete_form = DeleteForm()
    
    return render_template('index.html', 
                           emprendimientos=emprendimientos, 
                           form=delete_form,
                           count_si=count_si, 
                           count_no=count_no, 
                           count_error=count_error, 
                           count_total=count_total)

@app.route('/emprendimiento/delete/<int:emprendimiento_id>', methods=['POST'])
@login_required
@role_required('admin')
def delete_emprendimiento(emprendimiento_id):
    emprendimiento = Emprendimiento.query.get_or_404(emprendimiento_id)
    db.session.delete(emprendimiento)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/emprendimiento/new', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def new_emprendimiento():
    form = EmprendimientoForm()
    if form.validate_on_submit():
        print("Validación del formulario exitosa")
        print("Form Data:", form.data)
        try:
            nuevo_emprendimiento = Emprendimiento(
                run=form.run.data,
                rut=form.rut.data,
                nombre_emprendimiento=form.nombre_emprendimiento.data,
                razon_social=form.razon_social.data,
                nombre_representante=form.nombre_representante.data,
                correo_electronico=form.correo_electronico.data,
                telefono=form.telefono.data,
                direccion=form.direccion.data,
                provincia=form.provincia.data,
                comuna=form.comuna.data,
                estado=form.estado.data
            )

            nuevo_detalle = Detalle(
                emprendimiento=nuevo_emprendimiento,
                logo=form.logo.data,
                video=form.video.data,
                redes_sociales=form.redes_sociales.data,
                resena=form.resena.data,
                productos=form.productos.data,
                notas=form.notas.data  # Nuevo campo

            )

            db.session.add(nuevo_emprendimiento)
            db.session.add(nuevo_detalle)
            db.session.commit()
            print("Datos guardados en la base de datos")
            flash('Emprendimiento creado con éxito!')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al crear el emprendimiento: {e}', 'error')
            print(f'Error al crear el emprendimiento: {e}')
    else:
        print("Errores del formulario:", form.errors)
        
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error en el campo {getattr(form, field).label.text}: {error}", 'error')

    return render_template('emprendimiento_form.html', form=form, form_title="Nuevo Emprendimiento")

@app.route('/emprendimiento/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def edit_emprendimiento(id):
    emprendimiento = Emprendimiento.query.get_or_404(id)
    detalle = Detalle.query.filter_by(emprendimiento_id=id).first()
    form = EmprendimientoForm(obj=emprendimiento)

    if form.validate_on_submit():
        form.populate_obj(emprendimiento)

        # Actualizar los detalles del emprendimiento
        detalle.logo = form.logo.data
        detalle.video = form.video.data
        detalle.redes_sociales = form.redes_sociales.data
        detalle.resena = form.resena.data
        detalle.productos = form.productos.data
        detalle.notas = form.notas.data  # Nuevo campo

        db.session.commit()
        flash('Emprendimiento actualizado con éxito!')
        return redirect(url_for('index'))
    else:
        if detalle:
            form.logo.data = detalle.logo
            form.video.data = detalle.video
            form.redes_sociales.data = detalle.redes_sociales
            form.resena.data = detalle.resena
            form.productos.data = detalle.productos
            form.notas.data = detalle.notas  # Nuevo campo

    return render_template('emprendimiento_form.html', form=form, form_title="Editar Emprendimiento")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('index'))
        flash('Invalid username or password.')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
@login_required
@role_required('admin')
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, role=form.role.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/detalle/<int:emprendimiento_id>')
@login_required
def detalle(emprendimiento_id):
    emprendimiento = Emprendimiento.query.get_or_404(emprendimiento_id)
    detalles = Detalle.query.filter_by(emprendimiento_id=emprendimiento.id).all()
    return render_template('detalle.html', emprendimiento=emprendimiento, detalles=detalles)