# 🔒 Projeto de Autenticação e JWT com Flask

Este projeto é uma API de autenticação desenvolvida em Python utilizando o **Flask**. Ele oferece funcionalidades como registro de usuários, login e edição de saldo. A API utiliza **JWT (JSON Web Tokens)** para autenticação e controle de acesso, simulando operações de uma conta bancária.

## 🛠️ Tecnologias Utilizadas

- **🐍 Python**: Linguagem de programação principal do projeto.
- **🌐 Flask**: Framework web utilizado para criar a API.
- **💾 SQLite**: Banco de dados para armazenamento local de usuários e saldos.
- **🔑 JWT**: Gerenciamento de autenticação por meio de JSON Web Tokens.
- **🧪 Pytest**: Ferramenta para realizar testes automatizados.
- **🛡️ dotenv**: Gerenciamento de variáveis de ambiente.
- **🔧 Werkzeug**: Biblioteca utilizada para hashing de senhas e utilitários relacionados.

## 📋 Funcionalidades

1. **📝 Registrar Usuário**: Permite criar um novo usuário com login e senha.
2. **🔓 Login**: Autentica o usuário e retorna um JWT para acesso às funcionalidades protegidas.
3. **💰 Editar Saldo**: Permite que o usuário autenticado atualize o saldo.

## 🚀 Instalação e Execução

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/joschonarth/flask-auth-jwt
   cd flask-auth-jwt
   ```

2. **Crie um ambiente virtual** (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate # Linux/Mac
   venv\Scripts\activate # Windows
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**:
   Crie um arquivo `.env` na raiz do projeto e defina as seguintes variáveis:

   ```env
   KEY=my_key_123
   ALGORITHM=HS256
   JWT_HOURS=10
   ```

5. **Inicie o servidor**:

   ```bash
   python run.py
   ```

6. **Acesse a API**:
   A API estará disponível em `http://127.0.0.1:5000`.

## 🌐 Rotas

- **POST** - `/bank/register`: Registra um novo usuário.
  - Corpo da requisição:

    ```json
    {
      "username": "joschonarth",
      "password": "abcd1234"
    }
    ```

- **POST** - `/bank/login`: Realiza o login e retorna o JWT.
  - Corpo da requisição:

    ```json
    {
      "username": "joschonarth",
      "password": "abcd1234"
    }
    ```

- **PATCH** - `/bank/balance/:user_id`: Atualiza o saldo do usuário (autenticado).
  - Cabeçalho:

    ```json
    Authorization: Bearer <seu_jwt>
    ```

  - Corpo da requisição:

    ```json
    {
      "new_balance": 1500.0
    }
    ```

## ✅ Testes

O projeto inclui uma série de testes unitários e de integração para garantir a qualidade do código:

1. **Execute os testes**:

   ```bash
   pytest
   ```

2. **Visualize mais detalhes e mensagens do teste**:

   ```bash
   pytest -s -v
   ```

## Contribuições 🌟

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue com sugestões ou enviar um pull request com melhorias.

## 📞 Contato 

<div>
    <a href="https://www.linkedin.com/in/joschonarth/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
    <a href="mailto:joschonarth@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
</div>