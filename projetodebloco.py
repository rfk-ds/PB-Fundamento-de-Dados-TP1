# MENU
# ADICIONAR TAREFAS
# LISTAR TAREFAS
# MARCAR TAREFAS COMO CONCLUÍDAS
# REMOVER TAREFA

import datetime

tarefas = []

def adicionar_tarefa(descricao, prazo, urgencia):
    nova_tarefa = {
        "id": len(tarefas) + 1, #CORRIGIR: ID se repete caso eu exclua algum
        "descrição": descricao,
        "data_criação": datetime.datetime.now().date(),
        "prazo": prazo,
        "urgência": urgencia,
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
            prazo_formatado = f"{tarefa['prazo']['ano']}-{tarefa['prazo']['mês']}-{tarefa['prazo']['dia']}"
            print(f"\n| ID: {tarefa['id']} | Descrição: {tarefa['descrição']} | Data de criação: {tarefa['data_criação']} | Prazo: {prazo_formatado} | Urgência: {tarefa['urgência']} | Status: {tarefa['status']} |")

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

            print("\nDefina o prazo: ")
            dia = input("Dia: ")
            mes = input("Mês: ")
            ano = input("Ano: ")

            prazo = {
                "dia": dia,
                "mês": mes,
                "ano": ano
            }

            print("\nDefina a urgência: ")
            print("1 - Verde (não-urgente)")
            print("2 - Amarelo (urgênte)")
            print("3 - Vermelho (super urgente)")

            adicionar_tarefa(descricao, prazo)

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
