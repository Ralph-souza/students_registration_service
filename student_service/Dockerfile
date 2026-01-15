FROM python:3.9-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    postgresql-client \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependências Python
# Nota: requirements.txt está na raiz do projeto (contexto é a raiz)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação do student_service
COPY student_service/ .

# Criar diretório para arquivos estáticos
RUN mkdir -p /app/static

# Expor porta
EXPOSE 8000

# Comando padrão (pode ser sobrescrito no docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
