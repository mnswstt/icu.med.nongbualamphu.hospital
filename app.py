from flask import Flask, jsonify, request, render_template
from flask_socketio import SocketIO, emit
from flask_bootstrap import Bootstrap
import eventlet, socket, eventlet, functools
import db

app = Flask(__name__)
io = SocketIO(app, cors_allowed_origins="*")
bootstrap = Bootstrap(app)
eventlet.monkey_patch()

ip = '0.0.0.0'
port = 8888
server_address = (ip, port)

from urllib.request import urlopen
from urllib.error import URLError
def internet_on(host='http://google.com'):
    try:
        urlopen(host)
        return True
    except:
        return False

def patient_list(raw, d):
    for i in range(1, 21):
        d.append((raw["p"+str(i)], raw["d"+str(i)]))
    return d

@app.route('/', methods=['GET'])
def home():
    db.icu_floor3.insert_one({'GOOD':'BOY'})
    return render_template('index.html')

@app.route('/monitor')
def rpi_monitor():
    return render_template('monitor.html', isOnline=internet_on())

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        raw = request.form.to_dict(flat=True)
        io.emit('patient_list', {'patient_list': patient_list(raw, [])})
    return render_template('admin.html')

@io.on('connected')
def connected(mess='Client failed to connect'):
    print("Client connected,", mess)

def send_sensor_data(c):
    io.emit('sensor_data', c)

if __name__ == '__main__':
    import _thread, time
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(server_address)
    _thread.start_new_thread(lambda: io.run(app), ())

    while True:
        data, address = s.recvfrom(4096)
        send_sensor_data(data.decode('utf-8').splitlines()[0].split(','))
        time.sleep(1)
