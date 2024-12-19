class PessoaFisica:
    def __init__(self, id, renda_mensal, idade, nome_completo, celular, email, categoria, saldo):
        self.id = id
        self.renda_mensal = renda_mensal
        self.idade = idade
        self.nome_completo = nome_completo
        self.celular = celular
        self.email = email
        self.categoria = categoria
        self.saldo = saldo

    @staticmethod
    def sacar_dinheiro(valor, saldo):
        if valor > 1000:
            return "Erro: Limite de saque para pessoa física é R$ 1.000."
        if valor > saldo:
            return "Erro: Saldo insuficiente."
        return saldo - valor

    def realizar_extrato(self):
        return f"Extrato: Saldo disponível: R$ {self.saldo:.2f}"
