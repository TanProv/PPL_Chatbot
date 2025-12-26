from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from config import USERS

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in USERS and USERS[username]['password'] == password:
            session['user'] = username
            session['role'] = USERS[username]['role']
            flash('Đăng nhập thành công!', 'success')
            return redirect(url_for('public.index'))
        else:
            flash('Sai tài khoản hoặc mật khẩu!', 'error')
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Đã đăng xuất.', 'info')
    return redirect(url_for('auth.login'))