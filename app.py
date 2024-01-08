from flask import Flask, render_template, send_file, request, jsonify

from login_manager import login_manager, auth

from datalog import datalog

from udp_sender import UDPSender


udp_sender = UDPSender()

app = Flask(__name__)
app.config.from_pyfile('config.py')

login_manager.init_app(app)

app.register_blueprint(datalog)

app.register_blueprint(auth)

user_id = ""

block_user = True


# Rotas
@app.route('/')
def home():
    return render_template('login.html')



def get_client_ip():
    if 'X-Forwarded-For' in request.headers:
        user_ip = request.headers['X-Forwarded-For']
    else:
        user_ip = request.remote_addr
    return user_ip


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
