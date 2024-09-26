LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 1000
saldo = 0
operacoes = []
numero_saques = 0

def menu():

    while True:
        print("Operações disponíveis")
        print("Extrato (e)")
        print("Saque (s)")
        print("Depósito (d)")
        print("Sair (q)")
        print("Digite a operação desejada:")
        opcao = input()
    
        if opcao == 'e':
            extrato()
        elif opcao == 's':
            print("Digite o valor do saque")
            valor = input()
            if valor.isdigit():
                saque(float(valor))
            else: 
                print(30*'!' + '\n' +
                      "O valor digitado deve ser um número"
                      +'\n' + 30*'!'+ '\n')
        
        elif opcao == 'd':
            print("Digite o valor do deposito")
            valor = input()
            if valor.isdigit():           
                deposito(float(valor))
            else: 
                print(30*'!' + '\n' +
                    "O valor digitado deve ser um número"
                    +'\n' + 30*'!'+ '\n')
        elif opcao == 'q':
            break
        else:
            print(30*'!' + '\n' +
                  "Digite uma opção válida!" 
                  +'\n' + 30*'!'+ '\n')
    

def saque(valor):

    global saldo
    global numero_saques
    
    if (valor < saldo and valor < LIMITE_VALOR_SAQUE
        and numero_saques < LIMITE_SAQUES):
        
        saldo = saldo - valor
        numero_saques = numero_saques + 1
        operacoes.append(f"Saque de {valor:.2f}")
        
    else:
        print(30*'!' + '\n' +
            "Operação não pode ser concluída"
            +'\n' + 30*'!'+ '\n')
        menu()
      

def deposito(valor):

    global saldo
    
    saldo = saldo + valor
    operacoes.append(f"Depósito de {valor:.2f}")


def extrato():

    print( 30*'=' + '\n' + "Extrato" + '\n' + 30*'='+ '\n')

    for operacao in operacoes:
        print(operacao)
    print( 30*'=' + '\n' +
        f"Saldo: R$ {saldo:.2f}" '\n'+
        f"Saques disponíveis: {LIMITE_SAQUES - numero_saques}"
         +'\n' + 30*'='+ '\n')


if __name__ == "__main__":
    menu()