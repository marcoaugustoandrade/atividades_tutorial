from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://suporte:Suporte99@localhost/atividades'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__)) + "/static/uploads/"

from app.models import tables
from app.controllers import atividades

@app.route('/home')
def home():
    a = ['Semana ADS', 'Oficina GitHub']
    return render_template('index.html', atividades=a)
