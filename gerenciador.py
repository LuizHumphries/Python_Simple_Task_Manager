def add_task(tarefas: list[str], nome_tarefa: str) -> None:
    tarefa = {nome_tarefa: nome_tarefa, "completed": False}
    tarefas.append(tarefa)
    return

tarefas = []
while True:
    print("\n Menu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar Tarefa")
    print("4. Completar Tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")


    user_choice = input("Digite a sua escolha: ")
    if user_choice == "1":
        task_name = input("Digite o nome da tarefa que gostaria de adicionar: ")
        add_task(tarefas, task_name)
    elif user_choice == "6":
        break