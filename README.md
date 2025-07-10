# Remarkable Django Book Store
Take-home project for remarkable by Michael Lafortune. I decided to rename products to books just so I could keep it interesting. It has title/author/description search, as well as category, and tag filtering functionality.

# Prerequisites
- Python 3.x
- pip

# Installation

1. **Clone/download the project**
   git clone https://github.com/mlafortune123/Remarkable-Take-Home-Django

2. **Create virtual environment inside or outside the project**
   cd remarkable
   python3 -m venv venv
   source venv/bin/activate

3. **Install Django**
   pip install django

4. **Apply database migrations**
   python3 manage.py makemigrations products
   python3 manage.py migrate

5. **Create admin user**
   python3 manage.py createsuperuser

6. **Start the server**
   python3 manage.py runserver

## Project Structure

remarkable/
├─── manage.py
├─── config/
│    ├─── __init__.py
│    ├─── settings.py
│    ├─── urls.py
│    ├─── asgi.py
│    ├─── wsgi.py
│    └─── __pycache__/
├─── products/
│    ├─── __init__.py
│    ├─── models.py          # Book, Category, Tag models
│    ├─── views.py           # Search and filter logic
│    ├─── admin.py           # Admin interface config
│    ├─── apps.py
│    ├─── tests.py
│    ├─── urls.py            # URL routing
│    ├─── migrations/
│    ├─── __pycache__/
│    └─── templates/
│         └─── products/
│              └─── book_list.html
└─── db.sqlite3


## Models

- **Book**: Main model with title, author, description, price, etc.
- **Category**: Book categories (ForeignKey relationship)
- **Tag**: Book tags (ManyToMany relationship)

## Technologies Used

- Django 4.x
- SQLite (default database)
- Bootstrap 5 (UI styling)
- Python 3

## AI Disclosure

The html in book_list was initally AI generated then I expanded on it.