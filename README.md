# Django-CRM
*(Customer Relationship Management)*

The use of CRM by companies allows them to improve the sales performance of their products and services.  The more complex and time-consuming the sales process, the greater the improvement.  
This CRM is designed for individual use by any company. Access to the company's business data remains solely under its 
control.


Django CRM is an open-source [Django](https://www.djangoproject.com/start/overview/)-based project. It is written in 
Python (python crm).
Frontend is almost entirely based on the Django Templates.

## Main applications
CRM the project consists of the following **main applications**:

- products (services)
- ads (advertisements campaigns)
- leads (potential customers attracted by advertising)
- customers (active customers that signed the contract)

## Getting started
It is recommended to use web server and WSGI server (NGINX, UWSGI).  
This project is deployed as a regular django project.

Compatibility  
- Django 5.0.x
- Python 3.11+
- PostgreSQL 16+

## Project installation
To deploy the project, you will need: [Python](https://www.python.org/), and [PostgreSQL](https://www.postgresql.org)
database.

### Clone the project
```cmd
git clone https://github.com/DjangoCRM/django-crm.git
```
(the project will be cloned into the 'crm_system' folder)

### Install the requirements

It is recommended to first create a virtual environment:

```cmd
python3 -m venv ./myvenv
```

and activate it:

```cmd
cd ./myvenv/bin
source activate
cd ../../django-crm
```

then install the project requirements:

```cmd
pip install -r requirements.txt
```

## Settings
### Database
Specify details for connecting to a Postgres database.  
In the file `crm_system/settings.py` specify fields

- DB_TABLE_NAME
- DB_USER
- DB_PASSWORD

### Django
Once you installed the project and database execute

```cmd
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

now you have django super user which can get access to the admin page to specify users, groups and roles.

## Launch CRM on the development server
Don’t use this server in anything resembling a production environment.  
It’s intended only for use while developing.  

 ```cmd
python manage.py runserver
 ```

## Contributing
All types of contributions are welcome.
