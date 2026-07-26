# TaskFlow - Sistema de Gestão de Tarefas

## Sobre o Projeto

O TaskFlow é um sistema de gerenciamento de tarefas desenvolvido com **FastAPI** no backend e **React** no frontend, permitindo cadastro de usuários, autenticação segura com JWT e gerenciamento completo de tarefas.

O objetivo é permitir que usuários autenticados possam criar, visualizar, atualizar, concluir, reabrir e excluir suas próprias tarefas de forma simples, segura e organizada.

---

# Tecnologias Utilizadas

## Backend

* Python
* FastAPI
* SQLAlchemy
* SQLite
* JWT (JSON Web Token)
* Pydantic

## Frontend

* React
* Vite
* JavaScript
* CSS

## Versionamento

* Git
* GitHub

---

# Funcionalidades

## Usuários

* Cadastro de usuários
* Login com geração de Token JWT
* Senhas armazenadas com hash
* Proteção das rotas por autenticação

## Tarefas

* Criar tarefas
* Listar apenas as tarefas do usuário autenticado
* Editar tarefas
* Excluir tarefas
* Marcar tarefas como concluídas
* Reabrir tarefas concluídas
* Definir data de conclusão
* Feedback visual de sucesso e erro
* Interface responsiva

---

# Como Executar o Projeto

## 1. Clonar o repositório

```bash
git clone https://github.com/PDBD071/taskflow-management.git
```

---

# Backend

## Acessar a pasta

```bash
cd taskflow-management/backend
```

## Criar ambiente virtual

```bash
python -m venv venv
```

## Ativar ambiente virtual

### Windows

```bash
venv\Scripts\activate
```

## Instalar dependências

```bash
pip install -r requirements.txt
```

## Executar a API

```bash
uvicorn app.main:app --reload
```

A API ficará disponível em:

```
http://127.0.0.1:8000
```

---

# Frontend

## Acessar a pasta

```bash
cd taskflow-management/frontend
```

## Instalar dependências

```bash
npm install
```

## Executar o projeto

```bash
npm run dev
```

O frontend ficará disponível em:

```
http://localhost:5173
```

---

# Documentação da API

Após iniciar o backend, acesse:

```
http://127.0.0.1:8000/docs
```

A documentação Swagger permite testar todos os endpoints da API.

---

# Autenticação

O sistema utiliza autenticação via **JSON Web Token (JWT)**.

Fluxo de autenticação:

1. O usuário realiza o cadastro.
2. O usuário faz login.
3. A API gera um Token JWT.
4. O token é enviado nas requisições protegidas.
5. O usuário acessa apenas suas próprias tarefas.

---

# Estrutura do Projeto

```
taskflow-management
│
├── backend
│   ├── app
│   │   ├── controllers
│   │   ├── routes
│   │   ├── services
│   │   ├── security
│   │   ├── models.py
│   │   ├── schemas.py
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── database.db
│
├── frontend
│   ├── src
│   ├── public
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

# Variáveis de Ambiente

Crie um arquivo chamado **.env** utilizando como base o arquivo **.env.example**.

Exemplo:

```env
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

# Deploy

Atualmente o projeto é executado localmente e **não possui deploy publicado**.

---

# Autor

**Keli Cristina Silva Martins**

Projeto desenvolvido para o desafio **Fullstack – Sistema de Gestão de Tarefas**, utilizando **FastAPI**, **React**, **JWT**, **SQLite** e boas práticas de organização em camadas (Routes, Controllers e Services).
