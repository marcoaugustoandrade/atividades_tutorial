from app import app
from app import db
from flask import render_template
from flask import request
from flask import redirect
from app.models.tables import Atividade
from datetime import datetime
import uuid
import os


# Listando todas as atividades complementares
@app.route('/atividades')
def listar_atividades():
    a = Atividade.query.all()
    for i in range(len(a)):
        a[i].data = a[i].data.strftime('%d/%m/%Y')
    return render_template('atividades_listar.html', atividades=a)


# Listando uma atividade atraves do seu id
@app.route('/atividades/<int:atividade_id>')
def listar_atividade(atividade_id):
    a = Atividade.query.filter_by(id=atividade_id).first()
    a.data = a.data.strftime('%d/%m/%Y')
    return render_template('atividades_detalhe.html', atividade=a)


# Carregando o formulário para inserir uma nova atividade
@app.route('/atividades/novo')
def form_inserir_atividade():
    tipo = 'inserir'
    return render_template('atividades_formulario.html', tipo=tipo)


# Inserindo uma nova atividade
@app.route('/atividades/novo', methods=['POST'])
def inserir_atividade():

    # Recebendo o arquivo do formulário
    arquivo = request.files['arquivo']
    arquivo.filename = str(uuid.uuid4()) + os.path.splitext(arquivo.filename)[1]
    # TODO: trocar para o usuário logado
    pasta = app.config['UPLOAD_PATH'] + '1/'
    # TODO: transformar em função
    if not os.path.exists(pasta):
        os.mkdir(pasta)
    arquivo.save(pasta + arquivo.filename)

    # Colocando a data no padrão adequado
    data = datetime.strptime(request.form['data'], '%Y-%m-%d')

    # TODO: trocar para usuário logado
    a = Atividade(nome=request.form['nome'], tipo=request.form['tipo'], data=data,
                  carga_horaria=request.form['carga_horaria'], arquivo=arquivo.filename, usuario_id=1)
    db.session.add(a)
    db.session.commit()

    return redirect('/atividades/novo')


# Carregando o formulário para alterar uma atividade
@app.route('/atividades/alterar/<int:atividade_id>')
def form_alterar_atividade(atividade_id):
    tipo = 'alterar'
    return render_template('atividades_formulario.html', tipo=tipo)


# Alterando dados de uma atividade
@app.route('/atividades/alterar', methods=['POST'])
def alterar_atividade():
    return ""


# Deletar dados de uma atividade
@app.route('/atividades/deletar/<int:atividade_id>')
def deletar_atividade(atividade_id):
    a = Atividade.query.filter_by(id=atividade_id).first()
    # TODO: trocar para usuário logado
    os.remove(app.config['UPLOAD_PATH'] + '1/' + a.arquivo)
    db.session.delete(a)
    db.session.commit()
    return redirect('/atividades')
