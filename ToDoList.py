class ToDoList:
    # Código que monta uma lista de tarefas a se fazer do usuário
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        print(f'Tarefa "{tarefa}" adicionada com sucesso!')

    def listar_tarefas(self):
        if not self.tarefas:
            print('Nenhuma tarefa na lista.')
        else:
            print('Tarefas:')
            for i, tarefa in enumerate(self.tarefas, 1):
                print(f'{i}. {tarefa}')

    def remover_tarefa(self, indice):
        try:
            tarefa_removida = self.tarefas.pop(indice - 1)
            print(f'Tarefa "{tarefa_removida}" removida com sucesso!')
        except IndexError:
            print('Índice inválido. A tarefa não foi removida.')

def main():
    lista_de_tarefas = ToDoList()
    # Por se tratar de um sistema simples, ele não faz uso de interface gráfica

    while True:
        print('\n===== Gerenciador de Tarefas =====')
        print('1. Adicionar Tarefa')
        print('2. Listar Tarefas')
        print('3. Remover Tarefa')
        print('4. Sair')

        escolha = input('Escolha uma opção (1/2/3/4): ')

        if escolha == '1': 
            tarefa = input('Digite a tarefa: ')
            lista_de_tarefas.adicionar_tarefa(tarefa)
        elif escolha == '2':
            lista_de_tarefas.listar_tarefas()
        elif escolha == '3':
            indice = int(input('Digite o índice da tarefa a ser removida: '))
            lista_de_tarefas.remover_tarefa(indice)
        elif escolha == '4':
            print('Saindo do Gerenciador de Tarefas. Até logo!')
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')

if __name__ == "__main__":
    main()