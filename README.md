# API Aladdin Tapetes

API REST desenvolvida em Django afim de realizar consultas de preços de tapetes da loja Aladdin, e apresentar esses dados através da data solicitada de forma documentada.

## Requisitos

- Python 3.x instalado
- Git instalado

## Como rodar o projeto

### 1. Clone o repositório
```
git clone https://github.com/dev-miriambatista/api-rest-django-aladdin.git
cd api-rest-django-aladdin
```

### 2. Crie e ative o ambiente virtual
```
python -m venv venv
```

No Windows (PowerShell), antes de ativar execute:
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Depois ative:
```
venv\Scripts\activate
```

### 3. Instale as dependências
```
pip install -r requirements.txt
```

### 4. Configure o arquivo .env

Crie um arquivo `.env` na raiz do projeto com o conteúdo:
```
DEBUG=True
ALLOWED_HOSTS=127.0.0.1
```

### 5. Rode o servidor
```
py manage.py runserver
```

## Testes

Para rodar os testes unitários:
```
py manage.py test
```

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | /precos/?data=DD-MM-YYYY | Retorna preços de tapetes por data |

## Documentação

Acesse a documentação interativa Swagger em:
```
http://127.0.0.1:8000/swagger/
```
