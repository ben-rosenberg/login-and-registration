from flask_app import app, redirect, session

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('user/dashboard')
    return redirect('user/login')

