Programação Funcional
Atividade de Programação I (em duplas)
Prof. Dr. Antonio Marcos Selmini (antonio.selmini@espm.br)

Leia atentamente as instruções:
1. A atividade pode ser em duplas ou individual.
2. A entrega da atividade deve ser pelo github. Você deve enviar o link do repositório na área de entregas
do canvas.. É obrigatório a entrega dessa forma.
3. A data limite para entrega é dia 09/03/2025 às 23h59.

(5,0) Exercício 1: Gerenciamento de Entregas de um Serviço de Logística
Você está desenvolvendo um sistema para uma empresa de logística que precisa gerenciar a entrega
de pacotes. Cada pacote tem um código único, um destino (cidade) e um peso (em kg). Os pacotes
são organizados em um dicionário onde:
• A chave é o código do pacote (string).
• O valor é uma tupla contendo (cidade_destino, peso).
O programa deve fornecer as seguintes funcionalidades por meio de um menu de opções para o
usuário da aplicação.
a) Adicionar um novo pacote: O usuário informa o código do pacote, a cidade de destino e o peso.
O código do pacote não pode se repetir.
b) Remover um pacote: O usuário informa o código do pacote e ele deve ser removido da lista de
entregas.
c) Exibir os três pacotes mais pesados: Exibir uma lista dos três pacotes com maior peso.
d) Calcular o peso médio dos pacotes enviados para uma cidade específica: O usuário informa a
cidade, e o programa retorna a média do peso dos pacotes enviados para essa cidade.
e) Listar as três cidades com maior número de pacotes enviados: Exibir as cidades que mais recebem
pacotes ordenadas pela quantidade.

(5,0) Exercício 2: Simulação de Fila de Atendimento Prioritário
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
os N primeiros pacientes na ordem de prioridade correta
