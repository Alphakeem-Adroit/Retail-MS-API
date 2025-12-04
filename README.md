# Retail Management System (Products API)

A simple **Django REST Framework API** for managing and displaying products with multiple images.  
This project is designed for The A-M Global LTD that want to showcase products online without direct purchasing. Users can view products and contact the admin via WhatsApp.

---

## Features

- Add, view, and manage products via Django Admin
- Upload **multiple images per product**
- Public API endpoint to fetch products and their images
- Clean and simple API, no authentication required for read-only access
- Categorized products with descriptions and pricing
- Admin can easily manage all data from Django Admin dashboard

---

## Technologies Used

- **Backend:** Django, Django REST Framework
- **Database:** MySQL (development)
- **Media Storage:** Local `MEDIA_ROOT` (can be upgraded to cloud storage)

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/Alphakeem-Adroit/Retail-MS-API.git
cd Retail-MS-API
```

2. **Create a virtual environment and activate it**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure MySQL database**

Update `settings.py` with your database settings:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<your-db-name>',
        'USER': '<your-db-user>',
        'PASSWORD': '<your-db-password>',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

5. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create a superuser**

```bash
python manage.py createsuperuser
```

7. **Run the development server**

```bash
python manage.py runserver
```

---

## API Endpoints

* **List all products:**

```
GET /api/products/
```

* **Retrieve a single product by ID:**

```
GET /api/products/<id>/
```

Each product includes its **images**, `title`, `description`, `price`, `category`, and creation date.

---

## Media Settings (Development)

Uploaded images are stored locally in `media/products/`.
In `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Add to `urls.py`:

```python
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## Admin Panel

* Go to `http://127.0.0.1:8000/admin/`
* Login with your superuser credentials
* Add products and multiple images inline
* Changes immediately reflect in API endpoints

---

## Example API Response

```json
[
  {
    "id": 1,
    "title": "Wireless Headphones",
    "description": "High-quality sound and comfort",
    "price": "99.99",
    "category": "Electronics",
    "created_at": "2025-12-04T20:00:00Z",
    "images": [
      {
        "id": 1,
        "image": "http://127.0.0.1:8000/media/products/headphone1.jpg"
      },
      {
        "id": 2,
        "image": "http://127.0.0.1:8000/media/products/headphone2.jpg"
      }
    ]
  }
]
```

---

## Future Improvements

* Add **category filtering** and search in API
* Integrate **WhatsApp contact button** on frontend
* Optionally add authentication for admin-only API access
* Move media storage to cloud (S3, Cloudinary) for production

---

## License

MIT License © Alphakeem Adroit

```

---
