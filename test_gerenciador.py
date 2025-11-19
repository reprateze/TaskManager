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

def test_concluir_tarefa(gerente):
    gerente.adicionar(Tarefa(id="2", titulo="Pagar conta"))
    gerente.concluir("2")
    assert gerente.obter("2").concluida

def test_listar_pendentes_concluidas(gerente):
    gerente.adicionar(Tarefa(id="a", titulo="A"))
    gerente.adicionar(Tarefa(id="b", titulo="B"))
    gerente.concluir("b")
    pendentes = gerente.listar_pendentes()
    concluidas = gerente.listar_concluidas()
    assert len(pendentes) == 1 and pendentes[0].id == "a"
    assert len(concluidas) == 1 and concluidas[0].id == "b"

def test_editar_tarefa(gerente):
    gerente.adicionar(Tarefa(id="x", titulo="Old"))
    gerente.editar("x", titulo="Novo", descricao="desc")
    assert gerente.obter("x").titulo == "Novo"
    with pytest.raises(TarefaInvalidaErro):
        gerente.editar("x", titulo="")

def test_editar_data_vencimento_invalida(gerente):
    gerente.adicionar(Tarefa(id="d1", titulo="Vencimento"))
    with pytest.raises(TarefaInvalidaErro):
        gerente.editar("d1", data_vencimento="2025-01-01")

def test_buscar_por_titulo(gerente):
    gerente.adicionar(Tarefa(id="1", titulo="Comprar pão"))
    gerente.adicionar(Tarefa(id="2", titulo="Comprar leite"))
    gerente.adicionar(Tarefa(id="3", titulo="Estudar Python"))

    resultados = gerente.buscar_por_titulo("comprar")

    assert len(resultados) == 2
    assert resultados[0].id == "1"
    assert resultados[1].id == "2"
def test_listar_atrasadas(gerente):
    hoje = date.today()

    gerente.adicionar(Tarefa(id="1", titulo="T1", data_vencimento=hoje.replace(day=hoje.day - 2)))
    gerente.adicionar(Tarefa(id="2", titulo="T2", data_vencimento=hoje.replace(day=hoje.day + 3)))
    gerente.adicionar(Tarefa(id="3", titulo="T3", data_vencimento=hoje.replace(day=hoje.day - 1), concluida=True))

    atrasadas = gerente.listar_atrasadas()

    assert len(atrasadas) == 1
    assert atrasadas[0].id == "1"