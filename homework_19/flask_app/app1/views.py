from flask import Blueprint, render_template, request, abort
from requests import get
from datetime import datetime
from app1.validator import *

url = 'https://api.kanye.rest'

# Создание Blueprint
blueprint_name = Blueprint('blueprint_name', __name__)

# Определение маршрута и функции представления для Blueprint
@blueprint_name.route('/time')
def time():
    time_o = datetime.now().isoformat()
    return render_template('time.html', time_o = time_o)

@blueprint_name.route('/quote')
def quote():
    url = 'https://api.kanye.rest'
    quote_o = get(url).text
    return render_template('quote2.html', quote_o = quote_o)

@blueprint_name.route('/quote/<id>')
def quote_n(id):
    quote_o = []
    url = 'https://api.kanye.rest'
    for i in range(int(id)):
        quote_o.append(get(url).text)
    return render_template('quote.html', quote_o = quote_o)
    

@blueprint_name.route('/register', methods=["POST", "GET"])
def register():
    if request.method == 'POST':  
        d = dict(request.form)  
        try:
            username, password, email = d['login'], d['password'], d['email']
            if Validator(username, password, email).validate() == True: 
                return 'Valid'
            else:
                abort(406, 'ValidError')
        except KeyError as e:
            return f"Поле {e} не было передано"
    return render_template('register.html')

@blueprint_name.errorhandler(406)
def valid_error(error):
    return f"Valid_error"

