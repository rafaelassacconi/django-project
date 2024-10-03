# Django Surveys Project

### Requisitos
- [Miro: Surveys Project](https://miro.com/app/board/uXjVLX7sp2I=/?share_link_id=488501560439)

### Comandos

#### Criação do projeto
- `mkdir django-project` - cria pasta do projeto
- `cd django-project` - entra na pasta do projeto
- `python -m venv .venv` - cria virtualenv
- `source .venv/bin/activate` - ativa virtualenv
- `pip install Django` - instala Django

#### Criação da aplicação
- `django-admin startproject womakers` - cria projeto Django
- `cd womakers` - entra na pasta do sistema
- `python manage.py startapp surveys` - cria app

#### Migrações
- `python manage.py migrate` - executa migrações
- `python manage.py showmigrations` - mostra status das migrações
- `python manage.py sqlmigrate surveys 0001` - mostra SQL da migração

#### Outros
- `python manage.py runserver` - executa aplicação
- `python manage.py createsuperuser` - cria usuário do admin
- `python manage.py --help` - ver opções de comandos
- `python manage.py shell` - executa o console