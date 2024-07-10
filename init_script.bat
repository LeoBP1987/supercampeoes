@echo off
REM Instalar as dependências
pip install -r requirements.txt

REM Coletar arquivos estáticos
python manage.py collectstatic --noinput

REM Aplicar migrações
python manage.py migrate