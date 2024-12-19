from database import get_db_connection
from models.pessoa_fisica import PessoaFisica

class PessoaFisicaController:
    @staticmethod
    def listar_pessoas():
        conn = get_db_connection()
        pessoas = conn.execute("SELECT * FROM pessoa_fisica").fetchall()
        conn.close()
        return [dict(p) for p in pessoas]

    @staticmethod
    def sacar_dinheiro(id, valor):
        conn = get_db_connection()
        pessoa = conn.execute("SELECT * FROM pessoa_fisica WHERE id = ?", (id,)).fetchone()

        if not pessoa:
            return {"error": "Pessoa não encontrada"}, 404

        pessoa = dict(pessoa)
        novo_saldo = PessoaFisica.sacar_dinheiro(valor, pessoa["saldo"])

        if isinstance(novo_saldo, str):  # Erro
            return {"error": novo_saldo}, 400

        conn.execute("UPDATE pessoa_fisica SET saldo = ? WHERE id = ?", (novo_saldo, id))
        conn.commit()
        conn.close()

        return {"message": "Saque realizado com sucesso", "novo_saldo": novo_saldo}

    @staticmethod
    def realizar_extrato(id):
        conn = get_db_connection()
        pessoa = conn.execute("SELECT * FROM pessoa_fisica WHERE id = ?", (id,)).fetchone()
        conn.close()

        if not pessoa:
            return {"error": "Pessoa não encontrada"}, 404

        pessoa_obj = PessoaFisica(**dict(pessoa))
        extrato = pessoa_obj.realizar_extrato()

        return {"extrato": extrato}
