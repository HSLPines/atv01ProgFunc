
'''
Exercício 2: Simulação de Fila de Atendimento Prioritário
Você foi contratado para desenvolver um sistema de atendimento de um hospital que prioriza
pacientes de acordo com a gravidade do caso. O hospital mantém uma lista de pacientes em espera,
onde cada paciente tem um nome e uma prioridade de atendimento. Os pacientes são classificados
em três níveis de prioridade:
• Emergência (E): Deve ser atendido primeiro.
• Urgência (U): Atendido depois das emergências.
• Normal (N): Atendido por último.

Os pacientes são armazenados em uma lista de tuplas, onde cada tupla contém (nome_do_paciente,
prioridade).
O sistema deve realizar as seguintes operações por meio de um menu de opções:
a) Adicionar um paciente na lista: O paciente é inserido no final da lista.
b) Remover um paciente específico: O usuário informa o nome do paciente e ele é removido da lista.
c) Chamar os 3 próximos pacientes para atendimento: O programa deve exibir os três primeiros
pacientes da lista, priorizando primeiro Emergência (E), depois Urgência (U) e, por último, Normal
(N). Use slices para extrair os três primeiros pacientes ordenados corretamente.
d) Exibir os próximos N pacientes na fila: O usuário informa um número N, e o programa deve exibir
os N primeiros pacientes na ordem de prioridade correta.
'''

def ordenarFila(fila: list[tuple[str, str]]) -> list[tuple[str, str]]:

    prioridades = {'E': 1, 'U': 2, 'N': 3}
    
    def criterioOrdenacao(paciente: tuple[str, str]) -> int:
        return prioridades[paciente[1]]
    
    return sorted(fila, key=criterioOrdenacao)

def adicionarPaciente(fila: list[tuple[str, str]]) -> None:

    nome = input("Nome do paciente: ")
    prioridade = input("Prioridade (E/U/N): ").upper()
    
    if prioridade not in ('E', 'U', 'N'):

        print("Prioridade inválida!")
        return
    
    fila.append((nome, prioridade))
    print(f"Paciente {nome} adicionado com prioridade {prioridade}.")

def removerPaciente(fila: list[tuple[str, str]]) -> None:

    nome = input("Nome do paciente a remover: ")
    
    for paciente in fila:

        if paciente[0] == nome:

            fila.remove(paciente)
            print(f"Paciente {nome} removido da fila.")
            return
    
    print("Paciente não encontrado.")

def chamarProximos(fila: list[tuple[str, str]], quantidade: int = 3) -> None:

    if not fila:

        print("Fila vazia!")
        return
    
    filaOrdenada = ordenarFila(fila)
    chamados = filaOrdenada[:quantidade]
    
    for paciente in chamados:
        fila.remove(paciente)
    
    print("Próximos pacientes chamados:")
    for nome, prioridade in chamados:
        print(f"{nome} - Prioridade: {prioridade}")

def exibirProximos(fila: list[tuple[str, str]]) -> None:

    try:

        n = int(input("Quantos pacientes deseja visualizar? "))
        if not fila:

            print("Fila vazia!")
            return
        
        filaOrdenada = ordenarFila(fila)
        print("Próximos pacientes na fila:")
        for nome, prioridade in filaOrdenada[:n]:
            print(f"{nome} - Prioridade: {prioridade}")
    except ValueError:
        print("Erro: Insira um número válido.")

def main() -> None:

    fila: list[tuple[str, str]] = []
    
    while True:

        print("\n1. Adicionar paciente")
        print("2. Remover paciente")
        print("3. Chamar próximos 3 pacientes")
        print("4. Exibir próximos N pacientes")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionarPaciente(fila)
        elif opcao == '2':
            removerPaciente(fila)
        elif opcao == '3':
            chamarProximos(fila)
        elif opcao == '4':
            exibirProximos(fila)
        elif opcao == '5':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
    