from app import app
from flask import render_template
from app.models.tables import Atividade


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
    return ""


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
    return ""
