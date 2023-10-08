from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import sqlite3

app = Flask(__name__)
socketio = SocketIO(app)

def read_sensor_data():
    conn = sqlite3.connect('sensor_data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM sensor_data')
    data = c.fetchall()
    conn.close()
    print("Daten wurden gelesen:", data)
    return data

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    sensor_data = read_sensor_data()
    emit('sensor_data', sensor_data)

if __name__ == '__main__':
    socketio.run(app, host='192.168.1.100', debug=True)
