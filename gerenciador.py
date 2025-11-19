from datetime import date

# ===== EXCEÇÕES =====
class ErroTarefa(Exception):
    pass

class TarefaExisteErro(ErroTarefa):
    pass

class TarefaNaoEncontradaErro(ErroTarefa):
    pass

class TarefaInvalidaErro(ErroTarefa):
    pass

# ===== MODELO DE TAREFA =====
class Tarefa:
    def __init__(self, id, titulo, descricao="", concluida=False, data_vencimento=None):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = concluida
        self.data_vencimento = data_vencimento

# ===== GERENCIADOR DE TAREFAS =====
class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = {}

    def adicionar(self, tarefa: Tarefa):
        if not tarefa.id or not tarefa.titulo:
            raise TarefaInvalidaErro("ID e título são obrigatórios.")
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