from flask import Response
from flask_app.models.model_user import User
from flask_app import app, render_template, redirect, request, session


'''
DISPLAY: Login/registration page
'''
@app.route('/user/login')
def show_login_registration() -> str:
    if 'user_id' in session:
        return redirect('/user/dashboard')
    return render_template('login.html')

'''
ACTION: Login form, redirects to /user/dashboard
'''
@app.route('/user/validate_login', methods=['POST'])
def login() -> Response:
    is_valid = User.validate_user_login(request.form)
    if not is_valid:
        return redirect('/')
    return redirect('/user/dashboard')

'''
ACTION: Registration form, redirects to /user/dashboard
'''
@app.route('/user/validate_registration', methods=['POST'])
def register() -> Response:
    if not User.validate_user_registration(request.form):
        return redirect('/')
    session['user_id'] = User.create_user(request.form)
    return redirect('/user/dashboard')

'''
DISPLAY: User dashboard. Redirects to login/registration page if not logged in
'''
@app.route('/user/dashboard')
def dashboard() -> str:
    if not 'user_id' in session:
        return redirect('/user/login')
    this_user = User.get_user_by_id(session['user_id'])
    return render_template('dashboard.html', user=this_user)

'''
ACTION(?): Deletes user_id from session, thereby logging user out. Redirects
to login/registration page.
'''
@app.route('/user/logout')
def logout() -> Response:
    del session['user_id']
    return redirect('/')
