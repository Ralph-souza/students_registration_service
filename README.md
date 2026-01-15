# Students Registration Service

API de registro de alunos - Sistema de microserviços Django

## Arquitetura

Este projeto é composto por dois microserviços Django:

1. **Student Service** (`student_service/`) - Gerencia estudantes
2. **Registration Service** (`registration_service/`) - Gerencia registros de estudantes
3. **API Gateway** (`api_gateway/`) - Nginx como reverse proxy

## Tecnologias

- Django 4.1.4
- Django REST Framework 3.14.0
- PostgreSQL
- Nginx
- Docker & Docker Compose
- pytest
- pre-commit

## Estrutura do Projeto

```
students_registration_service/
├── student_service/          # Microserviço de estudantes
│   ├── apps/student/         # App Django
│   ├── tests/               # Testes
│   └── Dockerfile
├── registration_service/     # Microserviço de registros
│   ├── apps/registration/   # App Django
│   ├── tests/              # Testes
│   └── Dockerfile
├── api_gateway/            # API Gateway (Nginx)
├── docker-compose.yml      # Orquestração dos serviços
├── Makefile               # Comandos úteis
└── requirements.txt       # Dependências Python
```

## Pré-requisitos

- Python 3.9+
- Docker e Docker Compose
- PostgreSQL (ou usar via Docker)

## Instalação

### Desenvolvimento Local

1. Clone o repositório
2. Instale as dependências:
   ```bash
   make install
   # ou
   pip install -r requirements.txt
   ```

3. Configure as variáveis de ambiente (crie arquivos `.env` em cada serviço)

4. Execute as migrations:
   ```bash
   cd student_service && python manage.py migrate
   cd ../registration_service && python manage.py migrate
   ```

5. Execute os serviços:
   ```bash
   cd student_service && python manage.py runserver 8001
   cd registration_service && python manage.py runserver 8002
   ```

### Docker

```bash
docker-compose up -d
```

Veja [DOCKER.md](DOCKER.md) para mais detalhes.

## Testes

```bash
# Todos os testes
make test

# Testes específicos
make test-student
make test-registration
```

## Lint e Formatação

```bash
# Instalar hooks e executar
make lint

# Apenas executar
make pre-commit-run
```

## Endpoints

### Via API Gateway (porta 8000)
- Student Service: `http://localhost:8000/v1/api/student/`
- Registration Service: `http://localhost:8000/v1/api/registration/`
- Health Check: `http://localhost:8000/health`

### Direto nos serviços
- Student Service: `http://localhost:8001/api/student/`
- Registration Service: `http://localhost:8002/v1/api/registration/`

## Comandos Úteis

Ver `make help` para lista completa de comandos.

## Testando a API

### Postman

1. Importe a collection `POSTMAN_COLLECTION.json` no Postman
2. Configure a variável `base_url` para `http://localhost:8000` (API Gateway)
3. Siga o guia em [POSTMAN_GUIDE.md](POSTMAN_GUIDE.md) para testar todos os endpoints

### Swagger/OpenAPI

- Registration Service: `http://localhost:8002/v1/docs/` (quando rodando diretamente)
- Ou via API Gateway: `http://localhost:8000/v1/api/registration/` (se configurado)

## Documentação

- [DOCKER.md](DOCKER.md) - Guia de uso do Docker
- [POSTMAN_GUIDE.md](POSTMAN_GUIDE.md) - Guia completo de testes com Postman
