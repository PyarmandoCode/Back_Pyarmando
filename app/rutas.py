from app import app,db
from flask import request
from .models import Cursos

@app.route('/')
def hello():
    return {"hello": "world"}


@app.route('/cursos', methods=['POST', 'GET'])
def handle_cursos():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_curso = Cursos(curso=data['curso'], detalle=data['detalle'], tapa=data['tapa'],costo=data['costo'],inicio=data['inicio'],hora=data['hora'])

            db.session.add(new_curso)
            db.session.commit()

            return {"message": f"curso {new_curso.curso} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        cursos = Cursos.query.all()
        results = [
            {
                "curso": curso.curso,
                "detalle": curso.detalle,
                "tapa": curso.tapa,
                "costo": curso.costo,
                "inicio": curso.inicio,
                "hora": curso.hora
            } for curso in cursos]

        return {"count": len(results), "cursos": results, "message": "success"}
    
@app.route('/curso/<curso_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_curso(curso_id):
    curso = Cursos.query.get_or_404(curso_id)

    if request.method == 'GET':
        response = {
            "curso": curso.curso,
            "detalle": curso.detalle,
            "tapa": curso.tapa,
            "costo": curso.costo,
            "inicio": curso.inicio,
            "hora": curso.hora
          
        }
        return {"message": "success", "curso": response}

    elif request.method == 'PUT':
        data = request.get_json()
        curso.curso = data['curso']
        curso.detalle = data['detalle']
        curso.tapa = data['tapa']
        curso.costo = data['costo']
        curso.inicio = data['inicio']
        curso.hora = data['hora']
        db.session.add(curso)
        db.session.commit()

        return {"message": f"Curso {curso.curso} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(curso)
        db.session.commit()

        return {"message": f"Curso {curso.curso} successfully deleted."}

