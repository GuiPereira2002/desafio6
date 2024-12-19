from flask import Blueprint, jsonify, request
from controllers.pessoa_juridica_controller import PessoaJuridicaController

pessoa_juridica_bp = Blueprint("pessoa_juridica", __name__)

@pessoa_juridica_bp.route("/", methods=["GET"])
def listar_pessoas_juridicas():
    pessoas = PessoaJuridicaController.listar_pessoas()
    return jsonify(pessoas)

@pessoa_juridica_bp.route("/<int:id>/sacar", methods=["POST"])
def sacar_dinheiro(id):
    valor = request.json.get("valor")

    if not valor:
        return jsonify({"error": "Informe o valor a ser sacado"}), 400

    resultado, status = PessoaJuridicaController.sacar_dinheiro(id, valor)
    return jsonify(resultado), status

@pessoa_juridica_bp.route("/<int:id>/extrato", methods=["GET"])
def realizar_extrato(id):
    resultado = PessoaJuridicaController.realizar_extrato(id)
    return jsonify(resultado)
