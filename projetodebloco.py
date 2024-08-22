import datetime

tarefas = []

def adicionar_tarefa(descricao, prazo, prioridade):
    """
    Adiciona uma nova tarefa à lista de tarefas.

    A nova tarefa é criada com um ID, descrição, data de criação, prazo,
    prioridade e status inicial "Pendente". 

    Geração do ID da nova tarefa: se a lista de tarefas não estiver vazia
    um novo ID será gerado incrementando o maior ID presente na lista
    
    Parâmetros:
        descricao: A descrição da tarefa.
        prazo: O prazo para a conclusão da tarefa.
        prioridade: A prioridade da tarefa.

    Tarefa é adicionada à lista global `tarefas`.
    """
    if tarefas:
        novo_id = max(tarefa['id'] for tarefa in tarefas) + 1
    else:
        novo_id = 1

    nova_tarefa = {
        "id": novo_id,
        "descrição": descricao,
        "data_criação": datetime.datetime.now().date().strftime("%d - %B - %Y"),
        "prazo": prazo,
        "prioridade": prioridade,
        "status": "Pendente"
    }

    tarefas.append(nova_tarefa)
    print("\nTarefa adicionada!")

def listar_tarefas():
    """
    Exibe todas as tarefas cadastradas na lista de tarefas.

    A função verifica se há tarefas cadastradas e, caso existam, imprime uma lista formatada 
    com os detalhes de cada tarefa, incluindo ID, descrição, data de criação, prazo, prioridade e status.

    Se a lista de tarefas estiver vazia, uma mensagem informando que não há tarefas cadastradas é exibida.
    """
    if not tarefas:
        print("Não há tarefas cadastradas.")
    else:
        print("\n--------------- LISTA DE TAREFAS --------------\n")
        for tarefa in tarefas:
            print(f"\n| ID: {tarefa['id']} | Descrição: {tarefa['descrição']} | Criada em: {tarefa['data_criação']} | Prazo: {tarefa['prazo']} | Prioridade: {tarefa['prioridade']} | Status: {tarefa['status']} |")

def marcar_tarefa(id):
    """
    Marca uma tarefa com base no ID fornecido.

    A função percorre a lista de tarefas e altera o status da tarefa com o ID correspondente
    para "Concluída". Se a tarefa for encontrada e marcada, uma mensagem de sucesso é exibida.
    Caso contrário, uma mensagem informando que a tarefa não foi encontrada é mostrada.

    Parâmetros:
        id: O ID da tarefa a ser marcada como concluída.
    """
    for tarefa in tarefas:
        if tarefa['id'] == id:
            tarefa['status'] = "Concluída"
            print("\nTarefa marcada como concluída!")
            return

    print("\nTarefa não encontrada.")

def remover_tarefa(id):
    """
    Remove uma tarefa da lista de tarefas com base no ID fornecido.

    A função percorre a lista de tarefas e remove a tarefa cujo ID corresponde ao valor fornecido.
    Se a tarefa for encontrada e removida, uma mensagem de sucesso é exibida. Caso contrário, 
    uma mensagem informando que a tarefa não foi encontrada é mostrada.

    Parâmetros:
        id: O ID da tarefa a ser removida.
    """
    for tarefa in tarefas:
        if tarefa['id'] == id:
            tarefas.remove(tarefa)
            print("\nTarefa removida com sucesso!")
            return

    print("\nTarefa não encontrada.")

def menu():
    """
    A função apresenta um menu com opções para adicionar, listar, marcar como concluídas ou remover tarefas.
    O usuário pode selecionar uma opção digitando o número correspondente. 
    O menu continua sendo exibido até que o usuário selecione a opção de sair (0).

    Funcionalidades:
    - Adicionar tarefas: Permite ao usuário adicionar uma nova tarefa, especificando uma descrição, prazo e prioridade.
    - Listar tarefas: Exibe todas as tarefas cadastradas, com informações detalhadas.
    - Marcar tarefas como concluídas: Permite ao usuário marcar uma tarefa como concluída, identificando-a pelo ID.
    - Remover tarefas: Permite ao usuário remover uma tarefa da lista, identificando-a pelo ID.
    - Sair: Encerra o loop/programa.

    Tratamento de erros:
    - O código verifica a validade das entradas do usuário, garantindo que as opções sejam números inteiros válidos.
    - Mensagens de erro são exibidas para entradas inválidas, e o menu é redisponibilizado.
    """
    while True:
        print("\n--------------- MENU --------------\n")
        print("1 - Adicionar tarefas")
        print("2 - Listar tarefas")
        print("3 - Marcar tarefas como concluídas")
        print("4 - Remover tarefas")
        print("0 - SAIR")

        try:
            opcao = int(input("\nSelecione uma opção: "))
        
            if opcao == 1:
                descricao = input("Adicionar nova tarefa: ")

                print("\nPrazo da tarefa:")
                print("1 - Quando conveniente")
                print("2 - Em breve")
                print("3 - Imediato")

                while True:
                    try:
                        prazo = int(input("\nSelecione o número referente ao prazo: "))
                    except ValueError:
                        print("Seleção de prazo inválida. Preencha a informação utilizando um número inteiro.")

                    if prazo == 1:
                        prazo = "Quando conveniente"
                        break

                    elif prazo == 2:
                        prazo = "Em breve"
                        break

                    elif prazo == 3:
                        prazo = "Imediato"
                        break

                    else:
                        print(f"A opção {prazo} não existe.")
            
                print("\nNível de prioridade")
                print("1 - Baixa")
                print("2 - Média")
                print("3 - Alta")
            
                while True:
                    try:
                        prioridade = int(input("\nSelecione o número referente a prioridade: "))
                    except ValueError:
                        print("Nível de prioridade inválida. Preencha a informação utilizando um número inteiro.")

                    if prioridade == 1:
                        prioridade = "Baixa"
                        break

                    elif prioridade == 2:
                        prioridade = "Média"
                        break

                    elif prioridade == 3:
                        prioridade = "Alta"
                        break
                    
                    else:
                        print(f"A opção {prioridade} não existe")
            
                adicionar_tarefa(descricao, prazo, prioridade)
        

            elif opcao == 2:
                listar_tarefas()

            elif opcao == 3:
                try:
                    id = int(input("Selecione o ID da tarefa que deseja marcar como concluída: "))
                    marcar_tarefa(id)
                except ValueError:
                    print("\nID inválido. Faça seleção utilizando um número inteiro.")

            elif opcao == 4:
                try:
                    id = int(input("Selecione o ID da tarefa que deseja excluir: "))
                    remover_tarefa(id)
                except ValueError:
                    print("\nID inválido. Faça seleção utilizando um número inteiro.")

            elif opcao == 0:
                break

            else:
                print("\nOpção inválida.\n")
        except ValueError:
            print("\n\nSELEÇÃO INVÁLIDA! Escolha uma das opções utilizando um número INTEIRO.")

menu()