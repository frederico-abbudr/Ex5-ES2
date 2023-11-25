import unittest
from ToDoList import ToDoList
class TestToDoList(unittest.TestCase):

    def setUp(self):
        self.lista_de_tarefas = ToDoList()

    def test_adicionar_tarefa(self):
        self.lista_de_tarefas.adicionar_tarefa("Estudar Python")
        self.assertEqual(self.lista_de_tarefas.tarefas, ["Estudar Python"])

    def test_listar_tarefas(self):
        self.lista_de_tarefas.adicionar_tarefa("Fazer compras")
        self.lista_de_tarefas.adicionar_tarefa("Passear com o cachorro")
        
        import io
        from contextlib import redirect_stdout

        with io.StringIO() as buf, redirect_stdout(buf):
            self.lista_de_tarefas.listar_tarefas()
            output = buf.getvalue().strip()

        self.assertIn("1. Fazer compras", output)
        self.assertIn("2. Passear com o cachorro", output)

    def test_remover_tarefa(self):
        self.lista_de_tarefas.adicionar_tarefa("Ler livro")
        self.lista_de_tarefas.adicionar_tarefa("Fazer exercícios")
        
        self.lista_de_tarefas.remover_tarefa(1)
        self.assertEqual(self.lista_de_tarefas.tarefas, ["Fazer exercícios"])

    def test_remover_tarefa_com_indice_invalido(self):
        self.lista_de_tarefas.adicionar_tarefa("Estudar música")
        
        import io
        from contextlib import redirect_stdout

        with io.StringIO() as buf, redirect_stdout(buf):
            self.lista_de_tarefas.remover_tarefa(2)
            output = buf.getvalue().strip()

        self.assertIn("Índice inválido. A tarefa não foi removida.", output)
        self.assertEqual(self.lista_de_tarefas.tarefas, ["Estudar música"])

if __name__ == '__main__':
    unittest.main()