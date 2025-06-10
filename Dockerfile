FROM python:3.11-slim

WORKDIR /app

# Instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn uvicorn

# Copiar o código da aplicação
COPY . .

# Expor a porta que a aplicação usará
EXPOSE 8000

# Comando para iniciar a aplicação
CMD [ \
    "gunicorn", \
    "-w", "4", \
    "-k", "uvicorn.workers.UvicornWorker", \
    "app:create_app()", "-b", "0.0.0.0:8000"]