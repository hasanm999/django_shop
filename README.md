# Django Shop

A simple e-commerce website built with **Django**.

This project is a Django-based online shop that includes user authentication, products, shopping cart, checkout, orders, product ratings, profiles, and support tickets.

## Features

* User registration and login
* User profile
* Product listing
* Product details
* Product rating system
* Average product ratings
* Shopping cart
* Add, update and remove cart items
* Checkout system
* Order management
* Recent products
* Support ticket system
* User authentication
* Django admin panel
* Responsive frontend

## Technologies

* Python
* Django
* HTML
* CSS
* JavaScript
* Bootstrap
* SQLite

---

# Installation

Follow the steps below to run the project locally.

## 1. Clone the repository

Open your terminal or Command Prompt and run:

```bash
git clone https://github.com/hasanm999/django_shop.git
```

Then enter the project directory:

```bash
cd django_shop
```

GitHub's recommended workflow uses `git clone` to create a local copy of a repository and then `cd` to enter the cloned directory.

---

## 2. Switch to the `master` branch

This project uses the `master` branch for the version you want to run.

First, fetch the available branches:

```bash
git fetch --all
```

Then switch to `master`:

```bash
git checkout master
```

If your local Git version does not have the `master` branch yet, use:

```bash
git checkout -b master origin/master
```

You can verify the current branch with:

```bash
git branch
```

You should see:

```text
* master
```

Git branches allow different versions of a project to be maintained separately.

---

# 3. Create a Virtual Environment

It is recommended to use a virtual environment so that the project's Python packages remain isolated from other projects. Django's documentation also recommends using a virtual environment for local development.

### Windows

Run:

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

After activation, you should see something similar to:

```text
(venv)
```

at the beginning of your terminal line.

### macOS / Linux

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

# 5. Install Requirements

Install all required Python packages using the project's `requirements.txt` file:

```bash
pip install -r requirements.txt
```

A `requirements.txt` file is the standard pip format for specifying packages that should be installed for a project.

If you are using Windows, you can also use:

```bash
py -m pip install -r requirements.txt
```

---

# 6. Apply Database Migrations

Run Django migrations:

```bash
python manage.py makemigrations
```

Then:

```bash
python manage.py migrate
```

This will create and update the project's database tables.

---

# 7. Create a Superuser

If you want to access the Django administration panel, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the instructions in the terminal and enter:

* Username
* Email
* Password

After creating the account, you can access the Django admin panel from:

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

Open the following address in your browser:

```text
http://127.0.0.1:8000/
```

---

# 9. Project Structure

The project contains several Django applications responsible for different parts of the online shop.

A simplified structure looks like:

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

# 10. Useful Commands

### Start the server

```bash
python manage.py runserver
```

### Create migrations

```bash
python manage.py makemigrations
```

### Apply migrations

```bash
python manage.py migrate
```

### Create a superuser

```bash
python manage.py createsuperuser
```

### Check the current Git branch

```bash
git branch
```

### Switch to master

```bash
git checkout master
```

### Get the latest changes

```bash
git pull origin master
```

### Check Git status

```bash
git status
```

---

# 11. Updating the Project

If you already have the project installed and want to get the latest version from GitHub:

```bash
git checkout master
```

Then:

```bash
git pull origin master
```

After updating the project, run:

```bash
pip install -r requirements.txt
```

and:

```bash
python manage.py migrate
```

GitHub documents `git pull` as the standard way to retrieve and integrate changes from a remote repository.

---

# 12. Deactivate the Virtual Environment

When you are finished working on the project, you can deactivate the virtual environment with:

```bash
deactivate
```

---

# 13. Accessing the Project

After running the development server:

**Website**

```text
http://127.0.0.1:8000/
```

**Django Admin**

```text
http://127.0.0.1:8000/admin/
```

---

# Requirements

Make sure you have the following installed before starting:

* Python
* Git
* pip

The project dependencies are listed in:

```text
requirements.txt
```

---

# Author

**Hasan Mirzaie**

GitHub:

https://github.com/hasanm999

Project:

https://github.com/hasanm999/django_shop

---

# License

This project is for educational and development purposes.
