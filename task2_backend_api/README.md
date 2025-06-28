# 🛠️ Backend API with FastAPI, JWT Auth, and Role-Based Access

A secure, modular backend API built with FastAPI. Supports user authentication, role-based access control (RBAC), and serves data from a preprocessed CSV file.

---

## 📁 Project Structure
```
backend-api/
| |
│ ├── main.py 
│ ├── models.py 
│-├── database.py 
│ ├── schemas.py 
│ ├── auth.py 
│ ├── routes/
│ │ ├── users.py
│ │ └── data.py 
│ └── utils.py 
├── processed_data.csv 
├── requirements.txt
├── .env 
└── README.md
```


---

## 🚀 Features

✅ JWT Authentication  
✅ Role-Based Access (`user`, `admin`)  
✅ SQLAlchemy + SQLite (or PostgreSQL)  
✅ Protected API routes  
✅ Uses a real dataset (`processed_data.csv`)  
✅ Ready for containerization and deployment

---

## 🧪 API Endpoints

| Method | Endpoint        | Access     | Description                          |
|--------|------------------|------------|--------------------------------------|
| POST   | `/token`         | Public     | Login and receive JWT token          |
| GET    | `/data`          | User/Admin | View sample dataset records          |
| GET    | `/admin/data`    | Admin only | View data summary and diagnostics    |
| GET    | `/`              | Public     | Health check / welcome message       |

---


## 🧰 Getting Started

### 1. 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. ⚙️ Setup .env

#### Create a .env file in the root directory:

```
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=your_db_password
DATABASE_NAME=your_db_name
DATABASE_USERNAME=your_usename
SQL_LOGGING = false
SECRET_KEY=your_secret_key
```

### 3. ⚙️ Alembic Setup (for DB Migrations)
```
alembic init alembic
# Then in alembic/env.py
# import: from database import Base; from app import models
# set: target_metadata = Base.metadata

alembic revision --autogenerate -m "initial"
alembic upgrade head
```

### 4. 🚀 Run the App
```
uvicorn main:app --reload
```