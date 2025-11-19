import pytest
from datetime import date
from gerenciador import (
    GerenciadorTarefas,
    Tarefa,
    TarefaExisteErro,
    TarefaNaoEncontradaErro,
    TarefaInvalidaErro
)

@pytest.fixture
def gerente():
    return GerenciadorTarefas()

# ===== TESTES =====
def test_adicionar_tarefa(gerente):
    t = Tarefa(id="1", titulo="Comprar leite")
    gerente.adicionar(t)
    assert gerente.obter("1").titulo == "Comprar leite"

def test_adicionar_tarefa_invalida(gerente):
    with pytest.raises(TarefaInvalidaErro):
        gerente.adicionar(Tarefa(id="", titulo=""))

def test_adicionar_duplicada(gerente):
    gerente.adicionar(Tarefa(id="1", titulo="A"))
    with pytest.raises(TarefaExisteErro):
        gerente.adicionar(Tarefa(id="1", titulo="B"))

def test_remover_tarefa(gerente):
    gerente.adicionar(Tarefa(id="1", titulo="Tarefa"))
    gerente.remover("1")
    with pytest.raises(TarefaNaoEncontradaErro):
        gerente.obter("1")

def test_remover_inexistente(gerente):
    with pytest.raises(TarefaNaoEncontradaErro):
        gerente.remover("999")
