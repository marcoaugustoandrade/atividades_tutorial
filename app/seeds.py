from app import db
from app.models.tables import Usuario
from app.models.tables import Atividade
from datetime import date

u1 = Usuario(nome='marco', email='marco.andrade@ifro.edu.br', senha='Suporte99', admin=True)
db.session.add(u1)

a1 = Atividade(nome='Oficina GitHub', tipo='Oficina', data=date(2019, 10, 2), carga_horaria=8, arquivo='/1/1.pdf', usuario_id=1)
a2 = Atividade(nome='Big Data', tipo='Palestra', data=date(2020, 2, 10), carga_horaria=1, arquivo='/1/2.pdf', usuario_id=1)
a3 = Atividade(nome='Oficina Jekyll', tipo='Oficina', data=date(2020, 2, 11), carga_horaria=8, arquivo='/1/3.pdf', usuario_id=1)
db.session.add(a1)
db.session.add(a2)
db.session.add(a3)

db.session.commit()
