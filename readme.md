# Mini_Inventory_management_system

A small project using django and MySQL for learning working with django and MySQL and also deploying them.

---

## 🚀 Live Deployment

This project is deployed on **Railway**.

🔗 **Live URL:** [https://web-production-5b9c4.up.railway.app/](https://web-production-5b9c4.up.railway.app/)

---

## 📌 Features

* HTML & Tailwind
* MySQL database support

---

## 🛠️ Tech Stack

| Component  | Technology                     |
| ---------- | ------------------------------ |
| Backend    | Django                         |
| Frontend   | HTML , Bootstrap               |
| Database   | MySQL                          |
| Deployment | Railway.app                    |
| Storage    | Railway MySQL Database         |

---

## 📂 Project Structure

```

Mini_Inventory_management_system/
    manage.py
    inventory_project/
    inventory/
    templates/
    .env
    .gitignore
    Procfile
    requirements.txt
    runtime.txt
```



---

## 🧠 Environment Variables
Create a `.env` file in the Mini_Inventory_management_system:
```

MYSQL_DATABASE=railway
MYSQLUSER=<your_username>
MYSQLPASSWORD=<your_password>
MYSQLHOST=<ypur_host>
MYSQLPORT=port
DB_LIVE=False

```

---

## 📦 Installation & Setup
### 1. Clone the Repository
```

git clone ["https://github.com/Nishchal-Guptaa/Mini_Inventory_management_system.git"](https://github.com/Nishchal-Guptaa/Mini_Inventory_management_system.git)

cd repository

```

### 2. Create & Activate Virtual Environment
```

python -m venv venv

venv/Scripts/activate    # Windows

source venv/bin/activate # Linux/Mac

```

### 3. Install Requirements
```

pip install -r requirements.txt

```

### 4. Apply Migrations
```

python manage.py migrate

```

### 5. Run the Server
```

python manage.py runserver

```

---

## 🔑 Superuser
```

python manage.py createsuperuser

```

---


## 🛠 Deployment on Railway
Add **.env variables** in **Variables** section:


Start Command:
```

python manage.py migrate && gunicorn backend.wsgi

```

---

