# 📘 FAQ Management System

Welcome to the **FAQ Management System**, a Django-based API that allows users to create, manage, and retrieve multilingual FAQs. It includes WYSIWYG editor support, caching for performance optimization, and automated translations.

---

## 🌟 Features

- **CRUD operations for FAQs** (Create, Read, Update, Delete)
- **WYSIWYG Editor Support** using `django-ckeditor`
- **Multilingual Support** with automatic translations via `googletrans`
- **Fast Responses** with Redis caching
- **Django Admin Panel** for easy FAQ management
- **RESTful API** with language selection via `?lang=` query parameter
- **Comprehensive Testing** using `pytest`

---

## 🚀 Getting Started

### 1️⃣ Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- Django (>=5.1)
- Redis (for caching)

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/faq-management.git
cd faq-management
```

### 3️⃣ Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Run the Development Server
```bash
python manage.py runserver
```
Now visit `http://127.0.0.1:8000/admin/` to manage FAQs.

---

## 📌 API Endpoints

| Method | Endpoint        | Description |
|--------|----------------|-------------|
| GET    | `/api/faqs/`   | Fetch all FAQs |
| GET    | `/api/faqs/?lang=hi` | Fetch FAQs in Hindi |
| POST   | `/api/faqs/`   | Create a new FAQ |
| PUT    | `/api/faqs/{id}/` | Update an FAQ |
| DELETE | `/api/faqs/{id}/` | Delete an FAQ |



---


## 🧪 Running Tests
To ensure everything is working properly, run the test suite:
```bash
pytest --ds=faq_project.settings
```



Author :- @rohit110


