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
