# Assignment Django Project

This is a simple Django project for managing customers (Create, Read, Update, Delete).

## Features
- Add new customers  
- View customer list  
- Update existing customers  
- Delete customers with confirmation  

## Clone the Repo
```bash
git clone https://github.com/heroprogramm/Assignment_django.git
cd Assignment_django

````
##Setup & Run
pip install django
python manage.py migrate
python manage.py createsuperuser   # optional
python manage.py runserver

##project structure

myproject/
│── customers/ # App for customer CRUD
│── myproject/ # Main project settings
│── db.sqlite3 # Database file
│── manage.py # Django management script


