from flask import request, render_template, Response, redirect, url_for
import psutil, json

from app.main import main


@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        temp = 0
        with open('/sys/class/thermal/thermal_zone0/temp') as f:
            temp = float(f.read()) / 1000.0
        data = {
            'mem': psutil.virtual_memory().percent,
            'cpu': psutil.cpu_percent(interval=None, percpu=False),
            'net': round(temp, 1)
        }
        return json.dumps(data)
    return render_template('index.html')



