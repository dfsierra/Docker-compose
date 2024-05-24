# Dockerfile para el Contenedor 1 (Proxy)
FROM nginx:alpine

# Copiar archivo de configuración de Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Copiar archivos HTML y CSS a la carpeta del servidor web
COPY index.html /usr/share/nginx/html/
COPY styles.css /usr/share/nginx/html/
