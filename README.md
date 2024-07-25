# Your Random Facts API

## Descrição

**Your Random Facts API** é uma API simples que permite aos usuários criar perfis, descobrir fatos aleatórios, obter o fato do dia, salvar fatos interessantes e recuperar os fatos salvos. Os fatos são obtidos da API [Useless Facts](https://uselessfacts.jsph.pl/).

## Funcionalidades

- **Criar Usuário**: Crie um usuário fornecendo um nome e um nome de usuário.
- **Descobrir Fatos Aleatórios**: Obtenha fatos aleatórios sempre que quiser.
- **Descobrir o Fato do Dia**: Veja o fato especial do dia.
- **Salvar Fatos**: Salve os fatos que você achar interessantes.
- **Pegar Fatos Salvos**: Recupere e veja todos os fatos que você salvou anteriormente.

## Tecnologias Utilizadas

- **Python**
- **Flask**
- **SQLite**

## Requisitos

- Python 3.x
- SQLite

## Como Rodar

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/your-random-facts.git
    cd your-random-facts
    ```

2. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

3. Configure o banco de dados:

    ```bash
    python setup_db.py
    ```

4. Inicie a aplicação:

    ```bash
    python app.py
    ```

## Endpoints

[<img src="https://run.pstmn.io/button.svg" alt="Run In Postman" style="width: 128px; height: 32px;">](https://app.getpostman.com/run-collection/27937220-226384fe-26f3-4b41-8497-2ac256854f42?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D27937220-226384fe-26f3-4b41-8497-2ac256854f42%26entityType%3Dcollection%26workspaceId%3D23c49a4f-0121-47ad-8b9e-c430d997c508)

### Criar Usuário

- **URL**: `/users`
- **Método**: `POST`
- **Dados de Entrada**:
    ```json
    {
        "name": "John Doe",
        "username": "johndoe"
    }
    ```
- **Resposta de Sucesso**:
    ```json
    {
        "message": "User created"
    }
    ```

### Descobrir Fatos Aleatórios

- **URL**: `/facts/random`
- **Método**: `GET`
- **Resposta de Sucesso**:
    ```json
    {
        "id": "95b759d047e3bf8c88e08eaaf40880c1",
        "language": "en",
        "permalink": "https://uselessfacts.jsph.pl/api/v2/facts/95b759d047e3bf8c88e08eaaf40880c1",
        "source": "djtech.net",
        "source_url": "http://www.djtech.net/humor/useless_facts.htm",
        "text": "The only 15-letter word that can be spelled without repeating a letter is uncopyrightable."
    }
    ```

### Descobrir o Fato do Dia

- **URL**: `/fact_of_the_day`
- **Método**: `GET`
- **Resposta de Sucesso**:
    ```json
    {
        "id": "3b8c10e9cefa0eee8962ec37c9137459",
        "language": "en",
        "permalink": "https://uselessfacts.jsph.pl/api/v2/facts/3b8c10e9cefa0eee8962ec37c9137459",
        "source": "djtech.net",
        "source_url": "http://www.djtech.net/humor/useless_facts.htm",
        "text": "The first contraceptive was crocodile dung used by the ancient Egyptians."
    }
    ```

### Salvar Fatos

- **URL**: `/facts/save`
- **Método**: `POST`
- **Dados de Entrada**:
    ```json
    {
        "user_id": 1,
        "fact": {
            "id": "3b8c10e9cefa0eee8962ec37c9137459",
            "language": "en",
            "permalink": "https://uselessfacts.jsph.pl/api/v2/facts/3b8c10e9cefa0eee8962ec37c9137459",
            "source": "djtech.net",
            "source_url": "http://www.djtech.net/humor/useless_facts.htm",
            "text": "The first contraceptive was crocodile dung used by the ancient Egyptians."
        }
    }
    ```
- **Resposta de Sucesso**:
    ```json
    {
        "message": "Fact saved"
    }
    ```

### Pegar Fatos Salvos

- **URL**: `/facts/<username>`
- **Método**: `GET`
- **Resposta de Sucesso**:
    ```json
    {
        "facts": [
            {
                "id": "3b8c10e9cefa0eee8962ec37c9137459",
                "language": "en",
                "permalink": "https://uselessfacts.jsph.pl/api/v2/facts/3b8c10e9cefa0eee8962ec37c9137459",
                "source": "djtech.net",
                "source_url": "http://www.djtech.net/humor/useless_facts.htm",
                "text": "The first contraceptive was crocodile dung used by the ancient Egyptians."
            },
            {
                "id": "3b8c10e9cefa0eee8962ec37c9137459",
                "language": "en",
                "permalink": "https://uselessfacts.jsph.pl/api/v2/facts/3b8c10e9cefa0eee8962ec37c9137459",
                "source": "djtech.net",
                "source_url": "http://www.djtech.net/humor/useless_facts.htm",
                "text": "The first contraceptive was crocodile dung used by the ancient Egyptians."
            }
        ]
    }
    ```