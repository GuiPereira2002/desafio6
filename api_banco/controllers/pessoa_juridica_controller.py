from database import get_db_connection
from models.pessoa_juridica import PessoaJuridica

class PessoaJuridicaController:
    @staticmethod
    def listar_pessoas():
        conn = get_db_connection()
        pessoas = conn.execute("SELECT * FROM pessoa_juridica").fetchall()
        conn.close()
        return [dict(p) for p in pessoas]

    @staticmethod
    def sacar_dinheiro(id, valor):
        conn = get_db_connection()
        pessoa = conn.execute("SELECT * FROM pessoa_juridica WHERE id = ?", (id,)).fetchone()

        if not pessoa:
            return {"error": "Pessoa Jurídica não encontrada"}, 404

        pessoa = dict(pessoa)
        novo_saldo = PessoaJuridica.sacar_dinheiro(valor, pessoa["saldo"])

        if isinstance(novo_saldo, str):  # Erro
            return {"error": novo_saldo}, 400

        conn.execute("UPDATE pessoa_juridica SET saldo = ? WHERE id = ?", (novo_saldo, id))
        conn.commit()
        conn.close()

        return {"message": "Saque realizado com sucesso", "novo_saldo": novo_saldo}

    @staticmethod
    def realizar_extrato(id):
        conn = get_db_connection()
        pessoa = conn.execute("SELECT * FROM pessoa_juridica WHERE id = ?", (id,)).fetchone()
        conn.close()

        if not pessoa:
            return {"error": "Pessoa Jurídica não encontrada"}, 404

        pessoa_obj = PessoaJuridica(**dict(pessoa))
        extrato = pessoa_obj.realizar_extrato()

        return {"extrato": extrato}
