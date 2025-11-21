from db import criar_tabela, adicionar_gasto_db, listar_gastos, deletar_gastos

class ControleFinanceiro:
    def __init__(self):
        self.gastos=[]

    def adicionar_gasto(self, descricao, valor):
        self.gastos.append({"descricao": descricao, "valor": valor})

def main():
    criar_tabela()
    controle = ControleFinanceiro()


    while True:
        print("\n--Controle de Gastos--")
        print("1. Adicionar Gastos")
        print("2. Mostrar Gastos")
        print("3. Deletar Gasto")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            descricao = input("Digite a descrição: ")
            valor = float(input("Digite o valor: "))
            adicionar_gasto_db(descricao, valor)

        elif opcao == "2":
            listar_gastos()

        elif opcao =="3":
            deletar_gastos()


        elif opcao == "4":
            print("Saindo do programa...")
            break

        else:
            print("Opção incorreta, tente novamente")

if __name__ =="__main__":
    main()