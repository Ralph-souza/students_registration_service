# Docker Setup

Este projeto utiliza Docker Compose para orquestrar múltiplos serviços.

## Estrutura

- **2 Dockerfiles** (um para cada serviço Django):
  - `student_service/Dockerfile`
  - `registration_service/Dockerfile`
- **1 docker-compose.yml** na raiz que orquestra todos os serviços

## Serviços

1. **student-db**: Banco PostgreSQL para student_service (porta 5432)
2. **registration-db**: Banco PostgreSQL para registration_service (porta 5433)
3. **student-service**: Serviço Django para gerenciar estudantes (porta 8001)
4. **registration-service**: Serviço Django para gerenciar registros (porta 8002)
5. **api-gateway**: Nginx como API Gateway (porta 8000)

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com:

```env
# Student Service Database
STUDENT_DB_NAME=student_db
STUDENT_DB_USER=student_user
STUDENT_DB_PASSWORD=student_password

# Registration Service Database
REGISTRATION_DB_NAME=registration_db
REGISTRATION_DB_USER=registration_user
REGISTRATION_DB_PASSWORD=registration_password
```

## Comandos

### Subir todos os serviços
```bash
docker-compose up -d
```

### Ver logs
```bash
docker-compose logs -f
```

### Parar todos os serviços
```bash
docker-compose down
```

### Rebuild e subir
```bash
docker-compose up -d --build
```

### Executar migrations
```bash
docker-compose exec student-service python manage.py migrate
docker-compose exec registration-service python manage.py migrate
```

### Acessar o shell do container
```bash
docker-compose exec student-service bash
docker-compose exec registration-service bash
```

## Endpoints

- **API Gateway**: http://localhost:8000
  - Student Service: http://localhost:8000/v1/api/student/
  - Registration Service: http://localhost:8000/v1/api/registration/
  - Health Check: http://localhost:8000/health

- **Serviços diretos** (para desenvolvimento):
  - Student Service: http://localhost:8001/api/student/
  - Registration Service: http://localhost:8002/v1/api/registration/
