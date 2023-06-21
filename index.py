from flask import Flask, redirect, request, url_for, render_template
from mcrcon import MCRcon

IP = '127.0.0.1'
PORT = 25575
RCON_PASS = '20044200'

app = Flask(__name__)
mc =  MCRcon(IP, RCON_PASS, port=PORT)

@app.route('/')
def posrTest():
    return render_template('post.html')


def rcon_send(name, count):
    try:
        mc.connect()
        mc.command(f'say {name} - {count} ')
        mc.disconnect()
    except:
        return False
    return True

@app.route('/donate', methods=['POST', 'GET'])
def sosi():
    name = request.form['name']
    count = request.form['count']
    return render_template("status_return.html", status = str(rcon_send(name, count)))

if __name__ == '__main__':
    app.run(debug=False)