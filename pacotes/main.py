from GerenciadorDePacotes import GerenciadorDePacotes

def exibir_menu():
    print("Menu de Opções:")
    print("1. Adicionar um novo pacote")
    print("2. Remover um pacote")
    print("3. Exibir os três pacotes mais pesados")
    print("4. Calcular o peso médio dos pacotes enviados para uma cidade específica")
    print("5. Listar as três cidades com maior número de pacotes enviados")
    print("6. Sair")

def main():
    gerenciador = GerenciadorDePacotes()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            codigo = input("Informe o código do pacote: ")
            cidade_destino = input("Informe a cidade de destino: ")
            peso = float(input("Informe o peso do pacote (em kg): "))
            try:
                gerenciador.adicionar_pacote(codigo, cidade_destino, peso)
                print("Pacote adicionado com sucesso!")
            except ValueError as e:
                print(e)

        elif opcao == "2":
            codigo = input("Informe o código do pacote a ser removido: ")
            try:
                gerenciador.remover_pacote(codigo)
                print("Pacote removido com sucesso!")
            except ValueError as e:
                print(e)

        elif opcao == "3":
            pacotes = gerenciador.exibir_tres_pacotes_mais_pesados()
            print("Três pacotes mais pesados:")
            for codigo, (cidade, peso) in pacotes:
                print(f"Código: {codigo}, Cidade: {cidade}, Peso: {peso} kg")

        elif opcao == "4":
            cidade = input("Informe a cidade: ")
            peso_medio = gerenciador.calcular_peso_medio_por_cidade(cidade)
            print(f"Peso médio dos pacotes para {cidade}: {peso_medio} kg")

        elif opcao == "5":
            cidades = gerenciador.listar_tres_cidades_com_mais_pacotes()
            print("Três cidades com mais pacotes enviados:")
            for cidade, quantidade in cidades:
                print(f"Cidade: {cidade}, Quantidade de pacotes: {quantidade}")

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()