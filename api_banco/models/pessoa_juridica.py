class PessoaJuridica:
    def __init__(self, id, faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo):
        self.id = id
        self.faturamento = faturamento
        self.idade = idade
        self.nome_fantasia = nome_fantasia
        self.celular = celular
        self.email_corporativo = email_corporativo
        self.categoria = categoria
        self.saldo = saldo

    @staticmethod
    def sacar_dinheiro(valor, saldo):
        if valor > 10000:
            return "Erro: Limite de saque para pessoa jurídica é R$ 10.000."
        if valor > saldo:
            return "Erro: Saldo insuficiente."
        return saldo - valor

    def realizar_extrato(self):
        return f"Extrato: Saldo disponível: R$ {self.saldo:.2f}"
