# 🎬 Movies Django Project

A simple Django web application for managing movies.  
This project demonstrates core Django concepts such as models, views, forms, templates, and URL routing.

---

## 🚀 Features

- View list of movies
- Add new movies using Django forms
- Uses Django ORM for database operations
- Server-side rendering with Django templates
- Environment-based configuration using `.env`

---

## 🛠 Tech Stack

- **Backend:** Django 5.x
- **Language:** Python 3.x
- **Database:** SQLite (development)
- **Frontend:** Django Templates (HTML)

---

## 📂 Project Structure

movies/
├── movieList/
│ ├── migrations/
│ ├── templates/
│ │ └── movieList/
│ │ ├── index.html
│ │ └── addmovie.html
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ └── urls.py
├── movies/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── manage.py
└── .env


🔗 URL Endpoints

| URL           | Description |
| ------------- | ----------- |
| `/`           | Movie list  |
| `/moviesAdd/` | Add movie   |
| `/admin/`     | Admin panel |


🧪 Learning Objectives

- Django project vs app structure
- Function-based views (FBV)
- Django forms and validation
- URL routing
- Environment variables in Django