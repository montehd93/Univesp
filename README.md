# Univesp Projeto Integrador

Projeto integrador sobre doação, com objetivo de simplificar o acesso tanto de doadores quanto recebedores das doações.

O projeto utilizara django rest framework no backend com mysql como banco de dados e angular no front-end.

## Instalação

Efetuar o clone do git, de preferencia criar uma env do python para execução do projeto.

## Criação da env

Dentro da pasta do seu projeto deverá criar o seguinte comando.

Linux:

```bash
python3 -m venv nome_ambiente
```

Após criar o ambiente, deverá ativar ele com o seguinte comando:

```bash
source nome_ambiente/bin/activate
```

Windows:

```bash
python -m venv nome_ambiente
```

```bash
.\nome_ambiente\Scripts\Activate.ps1
```

## Windows Erro

Caso apresente o seguinte erro no windows ao criar o venv

    não pode ser carregado porque a execução de scripts foi desabilitada neste sistema.

Deverá executar o seguinte comando via powershell como administrador.
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser

Após isso, deverá confirmar no powershell para ativar e reutilizar o comando para criar o venv.

Após isso com o venv ativo, deverá ir até o path do arquivo requirements.txt e executar o comando abaixo.

```bash
pip install -r requirements.txt
```

# Banco de dados

Caso utilize docker, segue abaixo a configuração utilizada, lembrando que a configuração do path para os volumes foi configurado para Ubuntu 22.04 LTS

```
version: '3'

services:
  # MySQL
  db:
    container_name: mysql8
    image: mysql:8.0
    command: mysqld --default-authentication-plugin=mysql_native_password --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_ROOT_HOST: '%'
      MYSQL_DATABASE: donation
      MYSQL_ALLOW_EMPTY_PASSWORD: "no"
    ports:
      - '4406:3306'
    volumes:
      - '/var/lib/mysql8/db/data:/var/lib/mysql'
      - '/var/lib/mysql8/db/sql:/docker-entrypoint-initdb.d'
```
