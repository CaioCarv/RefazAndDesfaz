def pintar(listar):
    print('-' * 20)
    print('Tarefas: ')
    print(listar)
    print('-' * 20)


def add(tarefa, listar):
    listar.append(tarefa)
    print('Tarefa Adicionada com sucesso!')



def refaz(listar, refazer):
    if not refazer:
        print('Nada a refazer!')
        return
    last_ref = refazer.pop()
    listar.append(last_ref)
    print('Tarefa refeita!')


def desfaz(listar, refazer):
    if not listar:
        print('Nada a desfazer!')
        return
    last_item = listar.pop()
    refazer.append(last_item)
    print('Tarefa desfeita!')


if __name__ == '__main__':
    listar = []
    refazer = []

    while True:
        tarefa = input('Digite uma tarefa, "refazer", "desfazer", "listar" ou "stop" para sair: ').lower().strip()

        if tarefa == 'listar':
            pintar(listar)
            continue
        elif tarefa == 'desfazer':
            desfaz(listar, refazer)
            continue
        elif tarefa == 'refazer':
            refaz(listar, refazer)
            continue
        elif tarefa == 'stop':
            break
        add(tarefa, listar)
