from flask import Blueprint, jsonify, request
from controllers.pessoa_fisica_controller import PessoaFisicaController

pessoa_fisica_bp = Blueprint("pessoa_fisica", __name__)

@pessoa_fisica_bp.route("/", methods=["GET"])
def listar_pessoas_fisicas():
    pessoas = PessoaFisicaController.listar_pessoas()
    return jsonify(pessoas)

@pessoa_fisica_bp.route("/<int:id>/sacar", methods=["POST"])
def sacar_dinheiro(id):
    valor = request.json.get("valor")

    if not valor:
        return jsonify({"error": "Informe o valor a ser sacado"}), 400

    resultado, status = PessoaFisicaController.sacar_dinheiro(id, valor)
    return jsonify(resultado), status

@pessoa_fisica_bp.route("/<int:id>/extrato", methods=["GET"])
def realizar_extrato(id):
    resultado = PessoaFisicaController.realizar_extrato(id)
    return jsonify(resultado)
