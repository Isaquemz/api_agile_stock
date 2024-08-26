
# Agile Stock API

Esta é a versão 1.0.0 da API do Agile Stock, desenvolvida com Django. A API oferece funcionalidades para gerenciamento de estoque, incluindo operações CRUD em usuários, produtos, clientes, fornecedores, e outros recursos relacionados ao controle de estoque.

## Base URL

```
http://localhost:8000/
```

## Documentação da API

A documentação completa da API está disponível em:

```
http://localhost:8000/swagger/?format=openapi
```

## Endpoints Disponíveis

### Autenticação

- **Login**
  - `POST /auth_ag/login/`

- **Logout**
  - `GET /auth_ag/logout/`

### Gestão de Ações

- **Listar Ações**
  - `GET /auth_ag/acao/`

- **Criar Ação**
  - `POST /auth_ag/acao/`

- **Atualizar Ação**
  - `PUT /auth_ag/acao/`

- **Deletar Ação**
  - `DELETE /auth_ag/acao/`

- **Consultar Ação por ID**
  - `GET /auth_ag/acao/{id}/`

### Gestão de Funcionalidades

- **Listar Funcionalidades**
  - `GET /auth_ag/funcionalidade/`

- **Criar Funcionalidade**
  - `POST /auth_ag/funcionalidade/`

- **Atualizar Funcionalidade**
  - `PUT /auth_ag/funcionalidade/`

- **Deletar Funcionalidade**
  - `DELETE /auth_ag/funcionalidade/`

- **Consultar Funcionalidade por ID**
  - `GET /auth_ag/funcionalidade/{id}/`

### Gestão de Usuários

- **Listar Usuários**
  - `GET /auth_ag/usuario/`

- **Criar Usuário**
  - `POST /auth_ag/usuario/`

- **Atualizar Usuário**
  - `PUT /auth_ag/usuario/`

- **Deletar Usuário**
  - `DELETE /auth_ag/usuario/`

- **Consultar Usuário por ID**
  - `GET /auth_ag/usuario/{id}/`

### Gestão de Produtos

- **Listar Produtos**
  - `GET /produtos/`

- **Criar Produto**
  - `POST /produtos/`

- **Atualizar Produto**
  - `PUT /produtos/`

- **Deletar Produto**
  - `DELETE /produtos/`

- **Consultar Produto por ID**
  - `GET /produtos/{id}/`

### Gestão de Movimentações de Estoque

- **Listar Entradas**
  - `GET /movimentos/entrada/`

- **Criar Entrada**
  - `POST /movimentos/entrada/`

- **Atualizar Entrada**
  - `PUT /movimentos/entrada/`

- **Deletar Entrada**
  - `DELETE /movimentos/entrada/`

- **Consultar Entrada por ID**
  - `GET /movimentos/entrada/{id}/`

- **Listar Saídas**
  - `GET /movimentos/saida/`

- **Criar Saída**
  - `POST /movimentos/saida/`

- **Atualizar Saída**
  - `PUT /movimentos/saida/`

- **Deletar Saída**
  - `DELETE /movimentos/saida/`

- **Consultar Saída por ID**
  - `GET /movimentos/saida/{id}/`

## Licença

Este projeto está licenciado sob os termos da licença MIT.
