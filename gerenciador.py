from datetime import date

class ErroTarefa(Exception):
    pass

class TarefaExisteErro(ErroTarefa):
    pass

class TarefaNaoEncontradaErro(ErroTarefa):
    pass

class TarefaInvalidaErro(ErroTarefa):
    pass

def eh_primo(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
class Tarefa:
    def __init__(self, id, titulo, descricao="", concluida=False, data_vencimento=None):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = concluida
        self.data_vencimento = data_vencimento
class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = {}

    def adicionar(self, tarefa: Tarefa):
        if not tarefa.id or not tarefa.titulo:
            raise TarefaInvalidaErro("ID e título são obrigatórios.")
        if isinstance(tarefa.id, int) or (isinstance(tarefa.id, str) and tarefa.id.isdigit()):
            valor = int(tarefa.id)
            if not eh_primo(valor):
                raise TarefaInvalidaErro("ID numérico deve ser um número primo.")

        if tarefa.id in self.tarefas:
            raise TarefaExisteErro("Tarefa já existe.")
        self.tarefas[tarefa.id] = tarefa

    def obter(self, id):
        if id not in self.tarefas:
            raise TarefaNaoEncontradaErro("Tarefa não localizada.")
        return self.tarefas[id]

    def remover(self, id):
        if id not in self.tarefas:
            raise TarefaNaoEncontradaErro("Tarefa não localizada.")
        del self.tarefas[id]

    def concluir(self, id):
        self.obter(id).concluida = True

    def editar(self, id, titulo=None, descricao=None, data_vencimento=None):
        tarefa = self.obter(id)
        if titulo is not None:
            if not isinstance(titulo, str) or not titulo.strip():
                raise TarefaInvalidaErro("Título inválido.")
            tarefa.titulo = titulo
        if descricao is not None:
            tarefa.descricao = descricao
        if data_vencimento is not None:
            if not isinstance(data_vencimento, date):
                raise TarefaInvalidaErro("data_vencimento deve ser datetime.date")
            tarefa.data_vencimento = data_vencimento

    def listar_todas(self):
        return list(self.tarefas.values())

    def listar_pendentes(self):
        return [t for t in self.tarefas.values() if not t.concluida]

    def listar_concluidas(self):
        return [t for t in self.tarefas.values() if t.concluida]

    def buscar_por_titulo(self, termo):
        termo = termo.lower()
        return [
            t for t in self.tarefas.values()
            if termo in t.titulo.lower()
        ]
    def listar_atrasadas(self):
        hoje = date.today()
        return [
            t for t in self.tarefas.values()
            if t.data_vencimento is not None
            and t.data_vencimento < hoje
            and not t.concluida
        ]