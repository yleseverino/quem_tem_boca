# quemTemBoca 🐍

É um web app feito para encontrar facilmente os restaurantes próximos de você.

## Hosted

O app está hospedado na IBM Cloud utilizando a plataforma Cloud foundry, que é um serviço the (PaaS - Platform as a service), muito parecido com Heroku, só que com a diferença de ser totalmente Open source 😉.

link: [quemtemboca.mybluemix.net/](https://quemtemboca.mybluemix.net/)

## Requirements

- A Postgres Database
- S3 or (S3 Like) object sotarage (Optional)

## Geting started
1. Clonar o Repo:
    ```bash
    git clone https://github.com/yleseverino/quem_tem_boca.git
    ```
2. Mudar seu diretorio de trabalho:
    ```bash
    cd quem_tem_boca
    ```
3. Criar um venv para instalar as dependencias:
    ```bash
    python3 -m venv venv
    ```
4. Ativar seu ambiente virtual:
    ```bash
    source venv/bin/activate
    ```
6. Instalar os pacotes extras:
    ```
    pip install -r requirements.txt
    ```
7. Dar uma onlhada no arquivo de variaveis e criar o seu .env:
    ```bash
    cat .env.example > .env
    ```
    Sera necessario configurar a variavel de ambiente DATABASE_URL com a String the conneção da sua base de dado igual a representada no exemplo.
8. Rodar o app
    ```bash
    flask run
    ```
    Abrir o navegador em [localhost:5000](http://localhost:5000) e Voila! 🎉

## How to run the tests

1. Para rodar os testes basta instalar o modulos necessarios para rodar os testes:
    ```
    pip install -r requirements_tests.txt
    ```
2. Antes de rodar os teste é necessario sair e entrar novamente no ambiente virtual
    ```bash
    deactivate && source venv/bin/activate
    ```
3. E pronto só rodar o pytest:
    ```bash
    pytest
    ```
4. Para ter um relatorio detalhado da cobertura dos testes basta rodar o seguinde comando:
    ```bash
    pytest --cov-report html --cov=quemTemBoca test/   
    ```
5. Depois só abrir o arquivo index.html no seu navegador e ver o relatório.