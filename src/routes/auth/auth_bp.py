from flask import Blueprint, redirect, render_template, request, flash, url_for
from models.UsersModel import UsersModel


def auth_bp(mongo):
    auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')
    
    
    @auth_bp.route('/register', methods=['GET', 'POST'])
    def auth_register():
        if request.method == 'GET':
            return render_template('auth/register.html')
        
        # posts requests
        email = request.form.get('email')
        password = request.form.get('password')

        if UsersModel.user_exists(mongo, email):
            flash('El usuario ya existe')
            return render_template('auth/register.html'), 401
        
        if len(password) < 6 or len(password) > 12:
            flash('La contraseña no es válida.')
            return render_template('auth/register.html'), 401
        
        user_id = UsersModel.register_user(mongo, email, password)
        if user_id:
            redirect( url_for('auth_bp.auth_login') )

        return redirect( url_for('auth_bp.auth_register') )


    @auth_bp.route('/login', methods=['GET', 'POST'])
    def auth_login():
        if request.method == 'GET':
            return render_template('auth/login.html')
        
        email = request.form.get('email')
        password = request.form.get('passowrd')

        # se acabó el tiempo




    return auth_bp