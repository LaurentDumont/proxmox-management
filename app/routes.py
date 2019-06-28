#Flask imports
from app import app
from flask import render_template

#Application specific imports.
import requests
import json
import random

@app.route('/')
def get_prometheus():
    alert_screens = ['alert_1.gif', 'alert_2.gif', 'alert_3.gif', 'alert_4.gif', 'alert_5.gif', 'alert_6.gif']
    data = requests.get('http://g.cmaker.studio:9090/api/v1/alerts')
    json_data = json.loads(data.content)
    number_of_alerts = len(json_data['data']['alerts'])
    if number_of_alerts > 0:
        len(alert_screens)
        random_int = random.randint(0,5)
        print(random_int)
        alert_screen = alert_screens[random_int]
        return render_template('NOT-OK.html', alert_screen=alert_screen, title='ALERT! SHIT IS ON FIRE!')
    else:
        return render_template('OK.html', title='THINGS ARE FINE')
  