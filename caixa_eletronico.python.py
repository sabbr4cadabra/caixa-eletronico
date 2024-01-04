#Caixa Eletronico do Banco LouyseBank. 
#Estamos começando agora então ainda não temos muitos saques. 

class CaixaEletronico:

    def __init__(self, saldo):
        self.saldo = saldo

    def saque(self, valor):
        if valor > self.saldo:
            return False

        cédulas = []
        while valor > 0:
            if valor >= 50:
                cédulas.append(50)
                valor -= 50
            elif valor >= 20:
                cédulas.append(20)
                valor -= 20
            elif valor >= 10:
                cédulas.append(10)
                valor -= 10
            else:
                cédulas.append(1)
                valor -= 1

        return cédulas


def main():
    caixa = CaixaEletronico(1000)

    valor = int(input("Digite o valor do saque: "))
    cédulas = caixa.saque(valor)

    if not cédulas:
        print("Saldo insuficiente.")
    else:
        print("Saque efetuado com sucesso.")
        print("Cédulas:", cédulas)


if __name__ == "__main__":
    main()
    