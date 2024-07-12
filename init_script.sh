Copiar código
#!/bin/sh

# Instalar as dependências
echo "Instalando dependências..."
pip install -r requirements.txt

# Coletar arquivos estáticos
echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

# Aplicar migrações
echo "Fazendo migrações..."
python manage.py makemigrations
if [ $? -ne 0 ]; then
    echo "Erro ao fazer makemigrations"
    exit 1
fi

echo "Aplicando migrações..."
python manage.py migrate
if [ $? -ne 0 ]; then
    echo "Erro ao aplicar migrações"
    exit 1
fi

# Criar superusuário
echo "Criando superusuário..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell
if [ $? -ne 0 ]; then
    echo "Erro ao criar superusuário"
    exit 1
fi

echo "Script de inicialização concluído com sucesso"