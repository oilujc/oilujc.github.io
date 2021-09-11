Title: Configurar Django con Nginx, Gunicorn y Docker en Ubuntu
Date: 2020-10-15 10:20
Modified: 2020-10-15 10:20
Category: Python
Tags: Django, Python, Docker, Nginx
Slug: configurar-django-con-nginx-gunicorn-docker
Authors: Julio Martínez
Summary: Configurar entornos de producción con Django, Nginx, gunicorn y Docker.
cover_image: django.png

## Introducción

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum eu felis leo. Vivamus malesuada aliquet vehicula. Aliquam vel efficitur ex. Maecenas ut maximus mi. Integer sollicitudin egestas justo, quis consectetur velit pharetra non. Nunc ut bibendum dolor. Quisque varius, magna non viverra lobortis, risus ipsum fermentum neque, sit amet maximus dui nulla in augue. Phasellus eu libero at sem convallis faucibus. Sed condimentum tincidunt euismod. Vivamus vel elit ligula. Nullam eu turpis sit amet magna ullamcorper posuere in mattis sem. Vivamus ac ex tincidunt, vestibulum dolor non, dignissim libero. Praesent vehicula aliquet nisi eget blandit. Duis mollis turpis ac odio ultrices maximus. Quisque malesuada pharetra dictum. Duis hendrerit felis non massa consequat tempor.

## Instalar Docker 

```bash
sudo apt update
```

```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

```bash
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
```

```bash
sudo apt update
```

```bash
apt-cache policy docker-ce
```

```bash
sudo apt install docker-ce
```

```bash
sudo systemctl status docker
```

## Ejecutar el comando Docker sin sudo (Opcional)

## Instalar Docker Compose 
## Ejecución de un contenedor con Docker Compose

## Instalar Nginx
## Instalar Configurar el Firewall
## Verificar su servidor web
## Gestionar el proceso de Nginx
## Configurar los bloques del servidor (Recomendado)

## Fuentes