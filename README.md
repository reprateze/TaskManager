**Gerenciador de Tarefas – Projeto com Testes Unitários**

Este projeto implementa um Gerenciador de Tarefas em Python, focado em regras de negócio, validação de dados e cobertura com testes unitários utilizando Pytest.

O objetivo é demonstrar organização de código, boas práticas, tratamento de erros e automação de testes.

Domínio da Aplicação

A aplicação gerencia tarefas, permitindo:

Adicionar tarefas

Editar informações

Marcar como concluída

Remover tarefas

Buscar por título

Listar pendentes e concluídas

Listar tarefas atrasadas (com base na data de vencimento)

Cada tarefa possui:

id (único)

título

descrição

status (concluída ou não)

data de vencimento (opcional)

O sistema conta com validações completas e exceções específicas para erros comuns.

**Estrutura de Código**
✔ Tarefa

Representa a entidade principal do sistema.

✔ GerenciadorTarefas

Controla todas as tarefas, valida entradas e aplica regras de negócio.

✔ Exceções personalizadas

TarefaExisteErro

TarefaNaoEncontradaErro

TarefaInvalidaErro

**Testes Unitários**

Os testes foram implementados com Pytest e garantem o comportamento correto do sistema.
Eles cobrem:

✔ Adição de tarefas
✔ Exclusão e busca
✔ Conclusão de tarefas
✔ Edição com validações
✔ Listagem (pendentes, concluídas e todas)
✔ Casos de erro (ID duplicado, título inválido etc.)
✔ Funcionalidades adicionais:

Busca por título (buscar_por_titulo)

Listagem de tarefas atrasadas (listar_atrasadas)

Ao todo, o projeto contém 12 testes automatizados.

**Tecnologias Utilizadas**
✔Python 3
✔Pytest (framework de testes)
✔Programação orientada a objetos (POO)

**Como Executar o Projeto**
pip install pytest

**Executar os testes**
pytest -v

**Estrutura Recomendada do Projeto**
/TaskManager
│── gerenciador.py
│── test_gerenciador.py
│── README.md
│── requirements.txt (opcional)

**Conclusão**
O projeto entrega:
✔ Gerenciador de Tarefas funcional
✔ Regras de validação e tratamento de erros
✔ Testes unitários completos (mais que o mínimo exigido)
✔ Cobertura de cenários reais de uso



