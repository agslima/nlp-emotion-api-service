# Usar Python oficial
FROM python:3.10-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar requirements e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o backend para dentro do container
COPY . .

# Expõe a porta que o Flask roda
EXPOSE 5000

# Comando de execução
CMD ["python3", "server.py"]
