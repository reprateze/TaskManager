from dataclasses import dataclass
from datetime import date
from typing import Optional, Dict, List

class TarefaExisteErro(Exception):
    pass

class TarefaNaoEncontradaErro(Exception):
    pass

class TarefaInvalidaErro(Exception):
    pass


@dataclass
class Tarefa:
    id: str
    titulo: str
    descricao: str = ""
    data_vencimento: Optional[date] = None
    concluida: bool = False


class GerenciadorTarefas:
    def __init__(self) -> None:
        self._tarefas: Dict[str, Tarefa] = {}

    def adicionar(self, tarefa: Tarefa) -> None:
        # validação básica
        if not tarefa.id or not tarefa.titulo:
            raise TarefaInvalidaErro("ID e título são obrigatórios.")

        # não permitir duplicadas
        if tarefa.id in self._tarefas:
            raise TarefaExisteErro(f"Tarefa com ID {tarefa.id} já existe.")

        # ❌ NÃO verificar se o ID é primo aqui
        self._tarefas[tarefa.id] = tarefa

    def obter(self, id: str) -> Tarefa:
        try:
            return self._tarefas[id]
        except KeyError:
            raise TarefaNaoEncontradaErro("Tarefa não encontrada.")

    def remover(self, id: str) -> None:
        if id not in self._tarefas:
            raise TarefaNaoEncontradaErro("Tarefa não encontrada.")
        del self._tarefas[id]

    def concluir(self, id: str) -> None:
        tarefa = self.obter(id)
        tarefa.concluida = True

    def listar_pendentes(self) -> List[Tarefa]:
        return [t for t in self._tarefas.values() if not t.concluida]

    def listar_concluidas(self) -> List[Tarefa]:
        return [t for t in self._tarefas.values() if t.concluida]

    def editar(self, id: str, **campos) -> None:
        tarefa = self.obter(id)

        if "titulo" in campos:
            novo_titulo = campos["titulo"]
            if not novo_titulo:
                raise TarefaInvalidaErro("Título não pode ser vazio.")
            tarefa.titulo = novo_titulo

        if "descricao" in campos:
            tarefa.descricao = campos["descricao"]

        if "data_vencimento" in campos:
            nova_data = campos["data_vencimento"]
            if nova_data is not None and not isinstance(nova_data, date):
                raise TarefaInvalidaErro("data_vencimento deve ser um objeto date.")
            tarefa.data_vencimento = nova_data

    def buscar_por_titulo(self, termo: str) -> List[Tarefa]:
        termo = termo.lower()
        return [
            t for t in self._tarefas.values()
            if termo in t.titulo.lower()
        ]

    def listar_atrasadas(self) -> List[Tarefa]:
        hoje = date.today()
        return [
            t for t in self._tarefas.values()
            if t.data_vencimento is not None
            and t.data_vencimento < hoje
            and not t.concluida
        ]