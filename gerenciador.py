def add_task(tarefas: list[str], task_name: str) -> None:
    task = {"task": task_name, "completed": False}
    tarefas.append(task)
    return

def see_tasks(tasks: list[str]) -> None:
    print("\nTask List:")
    for count, task in enumerate(tasks, start = 1):
        task_name = task['task']
        status = "✅" if task["completed"] else " "
        print(f"{count}. [{status}] {task_name}")
    return




tasks = []
while True:
    print("\n Task Manager Menu:")
    print("1. Add task")
    print("2. See taks")
    print("3. Update Task")
    print("4. Complete Tasks")
    print("5. Delete all completed tasks")
    print("6. Quit")


    user_choice = input("Choose an option: ")
    if user_choice == "1":
        task_name = input("Digite o nome da tarefa que gostaria de adicionar: ")
        add_task(tasks, task_name)
    elif user_choice == "2":
        see_tasks(tasks)
    elif user_choice == "6":
        break