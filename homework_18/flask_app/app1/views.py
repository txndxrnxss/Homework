from flask import Blueprint, render_template
from requests import *
from datetime import datetime

url = 'https://api.kanye.rest'
# print(url.text)

# Создание Blueprint
blueprint_name = Blueprint('blueprint_name', __name__)

# Определение маршрута и функции представления для Blueprint
@blueprint_name.route('/time')
def time():
    time_o = datetime.now().isoformat()
    return render_template('time.html', time_o = time_o)

@blueprint_name.route('/quote')
def quote():
    quote_o = get(url).text
    return render_template('quote.html', quote_o = quote_o)