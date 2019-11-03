from flask import Flask,jsonify, request, make_response


app = Flask(__name__)

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
        return ''

    return make_response('could verfify', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

if __name__ == '__main__':
    app.run(debug=True)

