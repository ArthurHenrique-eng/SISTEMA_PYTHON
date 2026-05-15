# Sistema de Login — Python

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Interface-Tkinter-00d4ff?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Arquitetura-Clean%20Code-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge"/>
</p>

<p align="center">
  Sistema de autenticação desktop com interface gráfica, construído em Python puro.<br/>
  Desenvolvido com foco em organização de código, separação de responsabilidades e boas práticas.
</p>

---

## Índice

- [Sobre o projeto](#-sobre-o-projeto)
- [Funcionalidades](#-funcionalidades)
- [Estrutura do projeto](#-estrutura-do-projeto)
- [Como rodar](#-como-rodar)
- [Tecnologias](#-tecnologias)
- [Autor](#-autor)

---

## Sobre o projeto

Este projeto é um sistema de login desktop desenvolvido em Python, com interface gráfica construída
usando `tkinter`. O objetivo foi praticar a organização de código em módulos com responsabilidades
bem definidas, seguindo princípios de **Clean Code** e separação de camadas.

Ao realizar login com credenciais válidas, o sistema abre automaticamente uma URL no navegador padrão.

---

## Funcionalidades

- [x] Interface gráfica com tema escuro
- [x] Validação de usuário e senha
- [x] Limite de tentativas (bloqueio após 3 erros)
- [x] Redirecionamento para URL após login bem-sucedido
- [x] Módulos separados por responsabilidade
- [x] Configurações centralizadas em `config.py`

---

## Estrutura do projeto

```
SISTEMA_PYTHON/
│
├── main.py          # Ponto de entrada da aplicação
├── config.py        # Configurações globais (URL, cores, limites)
│
├── usuario.py       # Entidade de usuário
├── validacao.py     # Regras de autenticação
├── login.py         # Interface gráfica (janela de login)
├── app.py           # Controlador — liga todos os módulos
└── navegador.py     # Utilitário para abrir o navegador
```

Cada módulo tem uma única responsabilidade — nenhum arquivo conhece mais do que precisa.

---

## Como rodar

**Pré-requisito:** Python 3.10 ou superior instalado.

```bash
# 1. Clone o repositório
git clone https://github.com/ArthurHenrique-eng/SISTEMA_PYTHON.git

# 2. Acesse a pasta
cd SISTEMA_PYTHON

# 3. Execute
python main.py
```

> Nenhuma instalação de dependências necessária — o projeto usa apenas a biblioteca padrão do Python.

### Credenciais de teste

| Usuário  | Senha       |
|----------|-------------|
| arthur   | senha123    |
| admin    | admin@2024  |
| user     | 1234        |

---

## Tecnologias

| Tecnologia | Uso |
|---|---|
| [Python 3](https://www.python.org/) | Linguagem principal |
| [tkinter](https://docs.python.org/3/library/tkinter.html) | Interface gráfica |
| [webbrowser](https://docs.python.org/3/library/webbrowser.html) | Abertura de URL |

---

## Autor

Feito por **Arthur Henrique**

[![GitHub](https://img.shields.io/badge/GitHub-ArthurHenrique--eng-181717?style=flat-square&logo=github)](https://github.com/ArthurHenrique-eng)
