<h1>Assignment Django Project</h1>

This is a simple Django project for managing customers (Create, Read, Update, Delete).

<h1> Features</h1>
- Add new customers  
- View customer list  
- Update existing customers  
- Delete customers with confirmation  

## Clone the Repo
```bash
git clone https://github.com/heroprogramm/Assignment_django.git
cd Assignment_django

````
Setup & Run

pip install django

python manage.py migrate

python manage.py createsuperuser  
# optional
python manage.py runserver

<h2>project structure</h2>

myproject/
│── customers/  # App for customer CRUD

│── myproject/ # Main project settings

│── db.sqlite3 # Database file

│── manage.py # Django management script







