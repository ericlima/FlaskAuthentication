from flask import Flask,jsonify, request, make_response
from functools import wraps
import jwt
import datetime


app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisthesecretkey'

def token_required(f):
    return ''

@app.route('/unprotected')
def unprotected():
    print('ainda nao faz nada')
    return ''

@app.route('/protected')
def protected():
    return ''

@app.route('/login')
def login():
    auth = request.authorization

    if auth and auth.password == 'password':
        token = jwt.encode({'user': auth.username,
                            'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=30)
                            },app.config['SECRET_KEY'])

        return jsonify({'token': token.decode('UTF-8') } )

    return make_response('could verfify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

if __name__ == '__main__':
    app.run(debug=True)

