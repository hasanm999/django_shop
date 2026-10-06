# Django Shop 🛒

A simple e-commerce website built with **Django**.

This project is a basic online shop created to practice Django and understand how the different parts of an e-commerce application work together.

---

## ⚠️ Project Note

> **This project was developed in 10 days as a learning and practice project.**

Please don't expect this to be a huge, highly optimized, production-ready, or professionally engineered e-commerce platform. 😄

The project is intentionally kept **simple** and most features have been implemented in the simplest and most straightforward way possible.

The main purpose of this project was to learn and practice:

* Django fundamentals
* Django models
* Views and URLs
* Forms
* Templates
* User authentication
* User profiles
* Shopping cart
* Checkout
* Orders
* Product ratings
* Support tickets
* Static files
* Django admin
* Git and GitHub

There are definitely many things that could be improved, optimized, refactored, or implemented in a more advanced way.

That's okay.

This project is mainly a **learning project**, not a production-level e-commerce system.

**In short:**
This is a simple Django shop built in **12 days** to practice and understand the basics of developing a complete web application.

---

# Features

* User registration
* User login and logout
* User profile
* Product listing
* Product details
* Product rating system
* Average product ratings
* Shopping cart
* Add products to cart
* Update cart quantities
* Remove products from cart
* Checkout system
* Order management
* Recent products
* Support ticket system
* Django authentication
* Django admin panel
* Responsive frontend
* Static files and frontend assets

---

# Technologies

This project was built using:

* **Python**
* **Django**
* **HTML5**
* **CSS3**
* **JavaScript**
* **Bootstrap**
* **SQLite**
* **Git**
* **GitHub**

---

# Requirements

Before installing the project, make sure you have these installed:

* Python
* Git
* pip

You can check your Python installation with:

```bash
python --version
```

Check Git:

```bash
git --version
```

Check pip:

```bash
pip --version
```

---

# Installation

Follow the steps below to download and run the project locally.

## 1. Clone the Repository

Open your terminal or Command Prompt and run:

```bash
git clone https://github.com/hasanm999/django_shop.git
```

Then enter the project directory:

```bash
cd django_shop
```

---

# 2. Switch to the `master` Branch

The project version intended for this setup is on the `master` branch.

First, fetch the remote branches:

```bash
git fetch --all
```

Then switch to the `master` branch:

```bash
git checkout master
```

If the `master` branch does not exist locally yet, use:

```bash
git checkout -b master origin/master
```

You can check your current branch with:

```bash
git branch
```

You should see:

```text
* master
```

---

# 3. Create a Virtual Environment

Creating a virtual environment is recommended so that the project's Python packages are isolated from other Python projects.

## Windows

Run:

```bash
python -m venv venv
```

Then activate it:

```bash
venv\Scripts\activate
```

If activation was successful, you should see something similar to:

```text
(venv)
```

at the beginning of your terminal.

## macOS / Linux

Create the virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

# 4. Upgrade pip

After activating the virtual environment, upgrade pip:

```bash
python -m pip install --upgrade pip
```

---

# 5. Install Project Requirements

The required Python packages are listed in `requirements.txt`.

Install them with:

```bash
pip install -r requirements.txt
```

On Windows, you can also use:

```bash
py -m pip install -r requirements.txt
```

---

# 6. Create Database Migrations

Run:

```bash
python manage.py makemigrations
```

Then apply the migrations:

```bash
python manage.py migrate
```

This will create the required database tables for the Django applications.

---

# 7. Create a Superuser

If you want to access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

Django will ask you for:

* Username
* Email address
* Password

After creating the superuser, you can access the admin panel at:

```text
http://127.0.0.1:8000/admin/
```

---

# 8. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

You should see something similar to:

```text
Starting development server at http://127.0.0.1:8000/
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

---

# 9. Project URLs

After starting the server, you can access the main website at:

```text
http://127.0.0.1:8000/
```

Django admin:

```text
http://127.0.0.1:8000/admin/
```

---

# Project Structure

A simplified version of the project structure looks like this:

```text
django_shop/
│
├── accounts/
│   ├── migrations/
│   ├── templates/
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── cart/
│   ├── migrations/
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── orders/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── product/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── website/
│   ├── templates/
│   ├── urls.py
│   └── views.py
│
├── templates/
│   └── base/
│
├── static/
│
├── manage.py
├── requirements.txt
└── README.md
```

---

# Useful Django Commands

## Run the development server

```bash
python manage.py runserver
```

## Create migrations

```bash
python manage.py makemigrations
```

## Apply migrations

```bash
python manage.py migrate
```

## Create a superuser

```bash
python manage.py createsuperuser
```

## Open Django shell

```bash
python manage.py shell
```

---

# Useful Git Commands

## Check the current branch

```bash
git branch
```

## Switch to master

```bash
git checkout master
```

## Get the latest changes

```bash
git pull origin master
```

## Check repository status

```bash
git status
```

## Download remote branch information

```bash
git fetch --all
```

---

# Updating the Project

If you already cloned the project and want to get the latest version:

First make sure you are on the `master` branch:

```bash
git checkout master
```

Then pull the latest changes:

```bash
git pull origin master
```

After updating the project, it is recommended to install any new requirements:

```bash
pip install -r requirements.txt
```

Then apply any new database migrations:

```bash
python manage.py migrate
```

Finally, start the server:

```bash
python manage.py runserver
```

---

# Deactivate Virtual Environment

When you are finished working on the project, you can deactivate the virtual environment:

```bash
deactivate
```

---

# Development Workflow

A typical workflow for working on this project is:

```bash
git clone https://github.com/hasanm999/django_shop.git

cd django_shop

git fetch --all

git checkout master

python -m venv venv

venv\Scripts\activate

python -m pip install --upgrade pip

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

---

# GitHub Repository

GitHub Repository:

https://github.com/hasanm999/django_shop

Author:

**Hasan Mirzaie**

GitHub:

https://github.com/hasanm999

---

# Disclaimer

This project was created primarily for **learning, experimentation, and practicing Django development**.

It should not be considered a production-ready e-commerce application.

The code is intentionally simple, and there may be areas that could be improved in terms of:

* Architecture
* Security
* Performance
* Code organization
* UI/UX
* Validation
* Error handling
* Scalability
* Testing

As I continue learning and improving my Django skills, these areas can be refactored and improved in future versions.

---

# License

This project is provided for educational and learning purposes.
