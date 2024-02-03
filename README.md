# CONTROL OF CONTAINERS RARRAS SUPER TIENDAS S.A DE C.V
Web system for the control and administration of containers of the company Rarras Super Tiendas S.A DE C.V

[![made-with-python](https://img.shields.io/badge/Made%20with-python-1f425f.svg)](https://www.python.org/)[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/erickcasita/rarras-admin)[![GPL Licence](https://badges.frapsoft.com/os/gpl/gpl.png?v=103)](https://opensource.org/licenses/GPL-3.0/)
![Interfaz del software](https://raw.githubusercontent.com/erickcasita/rarras-admin/master/screenshots/screen1.png)

## Installation
Download the project from Github to a local folder

`https://github.com/erickcasita/rarras-admin.git`

### Create a virtual development environment

`python -m venv *name* `

### Install dependencies

`pip install -r requirements.txt`

### Create file .env with database configurations
```
POSTGRESQL_HOST = POSTGRESQL_HOST
POSTGRESQL_BD = POSTGRESQL_BD
POSTGRESQL_USER = POSTGRESQL_USER
POSTGRESQL_PASSWORD = POSTGRESQL_PASSWORD 
POSTGRESQL_PORT = POSTGRESQL_PORT

```
### Create the migrations

`python manage.py makemigrations`

### Apply migrations

`python manage.py migrate`

### Run server

`python manage.pu runserver`