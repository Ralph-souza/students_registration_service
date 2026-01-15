# Guia de Testes com Postman

## Como Rodar a Aplicação

### Opção 1: Docker Compose (Recomendado)

```bash
# Subir todos os serviços
docker-compose up -d

# Ver logs
docker-compose logs -f

# Parar serviços
docker-compose down
```

**Endpoints disponíveis:**
- API Gateway: `http://localhost:8000`
- Student Service (direto): `http://localhost:8001`
- Registration Service (direto): `http://localhost:8002`

### Opção 2: Desenvolvimento Local

#### Pré-requisitos
- Python 3.9+
- PostgreSQL rodando localmente
- Variáveis de ambiente configuradas

#### Student Service

```bash
cd student_service

# Configurar variáveis de ambiente (criar arquivo .env)
# DB_NAME=student_db
# DB_USER=student_user
# DB_PASSWORD=student_password
# DB_HOST=localhost
# DB_PORT=5432

# Instalar dependências
pip install -r ../requirements.txt

# Executar migrations
python manage.py migrate

# Rodar servidor
python manage.py runserver 8001
```

#### Registration Service

```bash
cd registration_service

# Configurar variáveis de ambiente (criar arquivo .env)
# DB_NAME=registration_db
# DB_USER=registration_user
# DB_PASSWORD=registration_password
# DB_HOST=localhost
# DB_PORT=5432
# STUDENT_SERVICE_URL=http://localhost:8001/api/student

# Instalar dependências
pip install -r ../requirements.txt

# Executar migrations
python manage.py migrate

# Rodar servidor
python manage.py runserver 8002
```

#### API Gateway (Nginx)

```bash
cd api_gateway
docker build -t api-gateway .
docker run -d -p 8000:8000 --name api-gateway api-gateway
```

## Importar Collection no Postman

1. Abra o Postman
2. Clique em **Import**
3. Selecione o arquivo `POSTMAN_COLLECTION.json`
4. A collection será importada com todas as requisições

## Variáveis de Ambiente no Postman

Após importar a collection, configure as variáveis:

1. Clique na collection "Students Registration API"
2. Vá na aba **Variables**
3. Configure:
   - `base_url`: `http://localhost:8000` (API Gateway) ou `http://localhost:8001` (Student Service direto) ou `http://localhost:8002` (Registration Service direto)
   - `student_id`: Deixe vazio (será preenchido automaticamente após criar um estudante)
   - `registration_id`: Deixe vazio (será preenchido automaticamente após criar um registro)

## Fluxo de Teste Recomendado

### 1. Health Check
- Execute `Health Check` para verificar se a API está rodando

### 2. Criar um Estudante
- Execute `Create Student` com o payload:
```json
{
    "name": "João Silva",
    "id_doc": "12345678901"
}
```
- **Copie o `id` retornado** e cole na variável `student_id` da collection

### 3. Listar Estudantes
- Execute `List Students` para ver todos os estudantes

### 4. Buscar Estudante por ID
- Execute `Get Student by ID` (usa a variável `student_id`)

### 5. Criar um Registro
- Execute `Create Registration` com o payload:
```json
{
    "student_id": "<cole o student_id aqui>",
    "email": "joao.silva@example.com",
    "phone": "11987654321",
    "gender": "male",
    "degree": "graduation",
    "contact_name": "Maria Silva",
    "contact_number": "11976543210",
    "relationship": "mother"
}
```
- **Copie o `id` retornado** e cole na variável `registration_id` da collection

### 6. Buscar Registros por Student ID
- Execute `Get Registrations by Student ID` para ver todos os registros de um estudante

### 7. Atualizar Registro
- Execute `Update Registration` ou `Partial Update Registration`

### 8. Deletar
- Execute `Delete Registration` ou `Delete Student`

## Valores Válidos para Campos

### Gender (gênero)
- `male` - Masculino
- `female` - Feminino
- `other` - Outro(a)

### Degree (escolaridade)
- `fundamental` - Fundamental completo
- `fundamental_na` - Fundamental incompleto
- `high_school` - Ensino médio completo
- `high_school_na` - Ensino médio incompleto
- `graduation` - Superior completo
- `graduation_na` - Superior incompleto
- `other` - Outro

### Relationship (relacionamento)
- `father` - Pai
- `mother` - Mãe
- `other` - Outro

## Endpoints Disponíveis

### Via API Gateway (porta 8000)

#### Student Service
- `GET /v1/api/student/` - Lista estudantes
- `POST /v1/api/student/` - Cria estudante
- `GET /v1/api/student/{id}/` - Busca estudante por ID
- `PUT /v1/api/student/{id}/` - Atualiza estudante
- `DELETE /v1/api/student/{id}/` - Deleta estudante

#### Registration Service
- `GET /v1/api/registration/` - Lista registros
- `POST /v1/api/registration/` - Cria registro
- `GET /v1/api/registration/{id}/` - Busca registro por ID
- `PUT /v1/api/registration/{id}/` - Atualiza registro completo
- `PATCH /v1/api/registration/{id}/` - Atualiza registro parcialmente
- `DELETE /v1/api/registration/{id}/` - Deleta registro
- `GET /v1/api/registration/by_student/?student_id={uuid}` - Busca registros por student_id

#### Health Check
- `GET /health` - Verifica se a API está funcionando

### Direto nos Serviços

#### Student Service (porta 8001)
- `GET /api/student/` - Lista estudantes
- `POST /api/student/` - Cria estudante
- etc.

#### Registration Service (porta 8002)
- `GET /v1/api/registration/` - Lista registros
- `POST /v1/api/registration/` - Cria registro
- etc.

## Exemplos de Payloads

### Criar Estudante
```json
{
    "name": "João Silva",
    "id_doc": "12345678901"
}
```

### Criar Registro (completo)
```json
{
    "student_id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "joao.silva@example.com",
    "phone": "11987654321",
    "gender": "male",
    "degree": "graduation",
    "contact_name": "Maria Silva",
    "contact_number": "11976543210",
    "relationship": "mother"
}
```

### Criar Registro (mínimo)
```json
{
    "student_id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "joao.silva@example.com",
    "phone": "11987654321"
}
```

### Atualizar Registro (PATCH)
```json
{
    "email": "novo.email@example.com",
    "phone": "11999999999"
}
```

## Troubleshooting

### Erro: "Estudante com ID não encontrado"
- Certifique-se de que o `student_id` existe no Student Service
- Verifique se o Student Service está rodando
- Verifique se a variável `STUDENT_SERVICE_URL` está configurada corretamente

### Erro de conexão
- Verifique se todos os serviços estão rodando
- Verifique as portas (8000, 8001, 8002)
- Verifique os logs: `docker-compose logs -f`

### Erro de validação
- Verifique se os valores dos campos estão corretos (gender, degree, relationship)
- Verifique se o email está em formato válido
- Verifique se o phone não está vazio
