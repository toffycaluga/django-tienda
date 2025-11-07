# Django Tienda — Mini CRUD con Autenticación (PostgreSQL)

Proyecto de ejemplo para **gestionar productos, categorías y etiquetas** con **login/registro/logout** y **UI Bootstrap**.

## Requisitos
- Python 
- PostgreSQL 


## Configuración rápida

```bash
# 1) Clonar e ingresar
git clone https://github.com/toffycaluga/django-tienda.git
cd django-tienda

# 2) Crear entorno e instalar deps
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Variables de entorno (ejemplo)
```.env

export DB_HOST=127.0.0.1
export DB_PORT=5432
export DB_NAME=tienda_db
export DB_USER=tienda_user
export DB_PASSWORD=tu_password_fuerte
export DEBUG=True
```

> Asegúrate de crear la DB/usuario en PostgreSQL con los mismos datos.

```sql
CREATE DATABASE tienda_db;
```

## Migraciones y usuario admin

```bash
python manage.py migrate
python manage.py createsuperuser
```

## Ejecutar

```bash
python manage.py runserver
# http://127.0.0.1:8000/
```

## Rutas principales

- `/` — Inicio
- `/login/` — Iniciar sesión
- `/register/` — Registro de usuarios
- `/logout/` — Cerrar sesión (**usa POST**)
- `/productos/` — Listado (filtro por q y categoría)
- `/productos/crear/` — Crear
- `/categorias/`, `/etiquetas/` — CRUDs básicos



⌨️ con ❤️ por [Abraham Lillo](htps://github.com/toffycaluga)