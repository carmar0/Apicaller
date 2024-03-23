# Usa la imagen oficial de Python de Alpine como base
FROM python:3.9-alpine

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo `main.py` y `requirements.txt` al directorio de trabajo en la imagen
COPY main.py requirements.txt ./

# Instala las dependencias definidas en requirements.txt
RUN apk add --no-cache gcc musl-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del gcc musl-dev

# Ejecuta el script `main.py` cuando se inicie el contenedor
CMD ["python", "main.py"]
