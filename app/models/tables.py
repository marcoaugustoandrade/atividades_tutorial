from app import db


class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200))
    email = db.Column(db.String(200), index=True, unique=True)
    senha = db.Column(db.String(200))
    admin = db.Column(db.Boolean)

    def __repr__(self):
        return '<Usuario %s>' % self.nome


class Atividade(db.Model):
    __tablename__ = 'atividades'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200))
    tipo = db.Column(db.String(200))
    data = db.Column(db.DateTime, nullable=False)
    carga_horaria = db.Column(db.Numeric, nullable=False)
    arquivo = db.Column(db.String(200), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    def __repr__(self):
        return '<Atividade %s>' % self.nome
