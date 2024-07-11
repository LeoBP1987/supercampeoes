#!/bin/sh

# Instalar as dependências
pip install -r requirements.txt

# Coletar arquivos estáticos
#python manage.py collectstatic --noinput

# Aplicar migrações
#python manage.py migrate

# Criar superusuário
#echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell