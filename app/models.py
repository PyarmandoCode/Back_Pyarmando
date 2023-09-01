from app import db


class Cursos(db.Model):
    idcurso = db.Column(db.Integer, primary_key=True)
    curso = db.Column(db.String())
    detalle = db.Column(db.Text)
    tapa = db.Column(db.String())
    costo = db.Column(db.Numeric(7,2))
    inicio = db.Column(db.String())
    hora = db.Column(db.String())

    # def __init__(self, curso,detalle, tapa, costo,inicio,hora):
    #     self.curso = curso
    #     self.detalle = detalle
    #     self.tapa = tapa
    #     self.costo = costo
    #     self.inicio=inicio
    #     self.hora = hora

    # def __repr__(self):
    #     return f"<Curso {self.curso}>"

