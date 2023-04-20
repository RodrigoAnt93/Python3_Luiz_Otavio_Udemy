#Criando um lista de atividades onde posso desfazer e refazer algo.
main_list = []
discard_list = []
while True:
    print('Command: list, undo, redo: ')
    choice = str(input('Enter a task or command: ')).lower().strip()
    if choice == 'undo':
        if main_list:
            discard_list.append(main_list.pop())
            print(f'Task {discard_list[-1]} removed from list.')
            print()
        else:
            print('Nothing to undo!')
    elif choice == 'redo':
        if discard_list:
            main_list.append(discard_list.pop())
            print(f'Task {main_list[-1]} added from list.')
            print('')
        else:
            print('Nothing to redo!')
    elif choice == 'list':
        if main_list:
            for item in main_list:
                print(f' - {item}')
            print()
        else:
            print('Empty list!')
    else:
        main_list.append(choice)
        print('Task added!')
        print()