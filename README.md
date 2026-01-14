# Automação de Processos de Cadastro via RPA com Python

## Descrição do Projeto

Este projeto implementa uma solução de **RPA (Robotic Process Automation)** para a inserção de dados em sistemas legados ou interfaces web. O desenvolvimento segue a metodologia apresentada pela **Hashtag Programação** durante a *Jornada Python (Aula 1)*.

---

## Tecnologias e Dependências

* **Linguagem:** Python 3.13+
* **Gerenciador de Ambiente:** `uv`
* **Bibliotecas de Automação:**

  * `PyAutoGUI` (interação com interface gráfica e periféricos)
* **Processamento de Dados:**

  * `Pandas` (leitura e tratamento de DataFrames)

---

## Estrutura do Projeto

A organização do projeto segue a estrutura:

```plaintext
powerUp/
├── .venv/              # Ambiente virtual gerenciado pelo uv
├── data/               # Base de Dados (CSV)
├── scripts/            # Scripts de utilidade e testes de leitura
├── src/                # Código-fonte principal do projeto
│   └── powerup/        # Módulo principal da aplicação
│       └── __init__.py
├── pyproject.toml      # Configuração de dependências e metadados (uv)
├── uv.lock             # Trava de versões de dependências
└── README.md
```

---

## Arquitetura da Solução

O fluxo de execução do bot está segmentado em cinco etapas lógicas:

1. **Sincronização de Interface**
   Configuração de intervalos globais (`pyautogui.PAUSE`) para compatibilidade com o tempo de resposta do sistema.

2. **Acesso ao Sistema**
   Automatização do navegador para alcance do endpoint de login.

3. **Autenticação**
   Preenchimento automatizado de credenciais de acesso.

4. **Processamento de Dataset**
   Leitura do arquivo CSV via `Pandas` para conversão em estrutura iterável (*DataFrame*).

5. **Ciclo de Inserção**
   Iteração sobre as linhas da tabela para preenchimento dos campos de **Código**, **Marca**, **Tipo**, **Categoria** e **Preços**.

---

## Procedimentos de Configuração (Ambiente `uv`)

### 1. Instalação e Sincronização

Para preparar o ambiente e instalar as dependências declaradas no `pyproject.toml`:

```bash
uv sync
```

### 2. Execução

Para executar o script principal de automação:

```bash
uv run scripts/main.py
```

---

## Mecanismos de Segurança

Conforme as diretrizes técnicas da biblioteca **PyAutoGUI**, o script possui um recurso de **Fail-Safe** ativo. A execução é interrompida imediatamente caso o operador desloque o cursor do mouse para qualquer extremidade da tela, prevenindo ações não supervisionadas em caso de erro de lógica ou inconsistência de interface.

---

## Créditos e Referências

A arquitetura lógica e os *datasets* utilizados foram providos pela **Hashtag Programação** como parte do conteúdo didático da *Jornada Python*. O sistema alvo para os testes de cadastro é de propriedade e manutenção da referida instituição.

Referência: [https://www.youtube.com/watch?v=0GDt-6H9NWM] 
Referência: [https://drive.google.com/drive/folders/1ERaraa4ZeXWFWo4K8oNJi4kY6aGZYdzw]
