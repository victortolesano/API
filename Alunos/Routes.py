import Server import app
from flask import jsonify

from Services import ListarAlunos
from Models import resposta
@app.route("/alunos", methods=["GET"])
def listStudensRoute():
    resposta.resposta["Status"]="200"
    resposta.resposta["Dados"]=Alunos.listStudents()
    resposta.resposta["Mensagem"]="Requisição feita com sucesso"
    return jsonify(resposta.resposta)
    
