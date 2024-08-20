import datetime

tarefas = []

def adicionar_tarefa(descricao, prazo, prioridade):
    nova_tarefa = {
        "id": len(tarefas) + 1, # CORRIGIR: ID se repete caso eu exclua algum
        "descrição": descricao,
        "data_criação": datetime.datetime.now().date().strftime("%d - %b - %Y"),
        "prazo": prazo,
        "prioridade": prioridade,
        "status": "Pendente"
    }

    tarefas.append(nova_tarefa)
    print("\nTarefa adicionada!")

def listar_tarefas():
    if not tarefas:
        print("Não há tarefas cadastradas.")
    else:
        print("\n--------------- LISTA DE TAREFAS --------------\n")
        for tarefa in tarefas:
            print(f"\n| ID: {tarefa['id']} | Descrição: {tarefa['descrição']} | Data de criação: {tarefa['data_criação']} | Prazo: {tarefa['prazo']} | Prioridade: {tarefa['prioridade']} | Status: {tarefa['status']} |")

def marcar_tarefa(id):
    for tarefa in tarefas:
        if tarefa['id'] == id:
            tarefa['status'] = "Concluída"
            print("\nTarefa marcada como concluída!")
            return
    print("\nTarefa não encontrada.")

def remover_tarefa(id):
    for tarefa in tarefas:
        if tarefa['id'] == id:
            tarefas.remove(tarefa)
            print("\nTarefa removida com sucesso!")
            return
    print("\nTarefa não encontrada.")

while True:
        print("\n--------------- MENU --------------\n")
        print("1 - Adicionar tarefas")
        print("2 - Listar tarefas")
        print("3 - Marcar tarefas como concluídas")
        print("4 - Remover tarrefas")
        print("0 - SAIR")

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
