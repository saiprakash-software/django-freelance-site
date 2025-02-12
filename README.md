# Django Freelance Site

A freelance job marketplace built with Django, supporting both MySQL and PostgreSQL. This guide explains how to view available jobs on the website.

## 🚀 How to View Jobs

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/saiprakash-software/django-freelance-site.git
cd django-freelance-site
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Database

Ensure you have **MySQL** or **PostgreSQL** installed and running. Create a database manually or use the following commands:

#### **For MySQL**
1. Open MySQL.
2. Run:
   ```sql
   CREATE DATABASE freelance_site;
   ```
3. Update `settings.py` with your MySQL credentials:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'freelance_site',
           'USER': 'your_mysql_username',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

#### **For PostgreSQL**
1. Open PostgreSQL.
2. Run:
   ```sql
   CREATE DATABASE freelance_site;
   ```
3. Update `settings.py` with your PostgreSQL credentials:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'freelance_site',
           'USER': 'your_postgres_username',
           'PASSWORD': 'your_postgres_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run the Development Server

```bash
python manage.py runserver
```

### 6️⃣ Open the Website

Go to:

```
http://127.0.0.1:8000/
```

You can now browse available jobs on the site.

---


