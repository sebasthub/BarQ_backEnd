# Use a imagem base do Python
FROM python:3.9

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install -r requirements.txt

# Copia todo o código fonte do projeto para o diretório de trabalho
COPY . .

# Define a porta que o contêiner irá expor
EXPOSE 8000

# Comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
