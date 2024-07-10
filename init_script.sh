#!/bin/sh

# Instalar as dependências
pip install -r requirements.txt

# Coletar arquivos estáticos
python manage.py collectstatic --noinput

# Aplicar migrações
python manage.py migrate