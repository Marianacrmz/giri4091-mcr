# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor en el directorio de trabajo
COPY requirements.txt .

# Instala las dependencias necesarias
RUN pip install -r requirements.txt

# Copia el archivo app.py al contenedor en el directorio de trabajo
COPY app.py .

# Expone el puerto en el que correrá la aplicación
EXPOSE 5001

# Define el comando por defecto para correr la aplicación
CMD ["python", "app.py"]
