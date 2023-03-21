from flask import Flask, render_template, redirect, url_for
import serial

import time
app = Flask(__name__)



ip = '192.168.1.132'
url_rd = ip
file_dash = ""

ench1 = 0
ench2 = 0
ench3 = 0
ench4 = 0


#rutas de paneles
@app.route('/led')
def set_dashboard():
    global file_dash
    global ip 
    file_dash = "temp_dash.html"
    return redirect(url_for('main'))


@app.route('/dashboard')
def dashboard():
    global file_dash
    if (file_dash == ""):
        return "<html></html>"
    else:
        return render_template(file_dash, js_ip=url_rd)

@app.route('/')
def main():
    return render_template("index.html", js_ip=url_rd)
@app.route('/h1')
def h1():
    ser = serial.Serial('/dev/ttyACM0', 9600)
    time.sleep(2)  # wait for the serial connection to initialize
    global ench1; 
    if (ench1 != 1):
        message = "1"
        ench1 = 1
    else:
        message = "2"
        ench1 = 0
    ser.write(message.encode())  # encode the message as bytes and send it to the serial port
    line = ser.readline().decode('utf-8').rstrip()
    print(line)
    return redirect(url_for("dashboard"))


if __name__ == '__main__':
    app.run(f'{ip}', 80)
