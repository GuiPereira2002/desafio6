import unittest
from controllers.pessoa_juridica_controller import PessoaJuridicaController
from database import get_db_connection, init_db

class TestPessoaJuridicaController(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Inicializar o banco de dados com o schema e dados iniciais
        init_db()

    def test_listar_pessoas(self):
        pessoas = PessoaJuridicaController.listar_pessoas()
        self.assertTrue(len(pessoas) > 0)

    def test_sacar_dinheiro_valido(self):
        # Testar saque com valor dentro do limite
        resultado, status = PessoaJuridicaController.sacar_dinheiro(1, 5000)
        self.assertEqual(status, 200)
        self.assertIn("novo_saldo", resultado)

    def test_sacar_dinheiro_limite(self):
        # Testar saque acima do limite de R$ 10.000
        resultado, status = PessoaJuridicaController.sacar_dinheiro(1, 15000)
        self.assertEqual(status, 400)
        self.assertIn("error", resultado)

    def test_sacar_dinheiro_saldo_insuficiente(self):
        # Testar saque com saldo insuficiente
        resultado, status = PessoaJuridicaController.sacar_dinheiro(1, 1000000)
        self.assertEqual(status, 400)
        self.assertIn("error", resultado)

    def test_realizar_extrato(self):
        # Testar a geração de extrato
        resultado = PessoaJuridicaController.realizar_extrato(1)
        self.assertIn("extrato", resultado)

if __name__ == "__main__":
    unittest.main()
