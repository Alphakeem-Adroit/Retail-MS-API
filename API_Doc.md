# Retail Management System - API Documentation

This documentation covers the **public REST API** for managing and fetching products with multiple images.  
The API is built with **Django REST Framework** and is read-only for public access.

---

## Base URL

```

[http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

```

All endpoints are prefixed with `/api/`.

---

## Endpoints

### 1. List All Products

**Request**

```

GET /products/

```

**Description:**  
Fetches a list of all products, including their multiple images, title, description, category, price, and creation date.

**Response Example**

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

### 2. Retrieve a Single Product

**Request**

```
GET /products/<id>/
```

**Description:**
Fetches a single product by its `id` along with all associated images.

**URL Parameters**

| Parameter | Type | Description       |
| --------- | ---- | ----------------- |
| id        | int  | ID of the product |

**Response Example**

```json
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
```

---

### 3. (Admin-only) Create / Manage Products

**URL:**

```
http://127.0.0.1:8000/admin/
```

**Description:**
All product and image management is done via the **Django Admin panel**. Admins can:

* Create products
* Upload multiple images per product
* Edit or delete products and images

> Note: There is no public API endpoint for creating products or images. All modifications are handled by the admin.

---

## Media Files

* Uploaded images are stored at:

```
http://127.0.0.1:8000/media/products/<filename>
```

* Example:

```
http://127.0.0.1:8000/media/products/headphone1.jpg
```

* Ensure that `MEDIA_URL` and `MEDIA_ROOT` are correctly configured in `settings.py` for development:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

---

## Notes

* No authentication is required for **public GET requests**.
* Admin must use Django admin panel for **CRUD operations**.
* Responses include all images linked to a product as an array of objects.
* All prices are returned as strings to preserve decimal precision.

---

## Future Improvements

* Adding **search and filter endpoints** by category or price range.
* Adding **WhatsApp contact integration** for each product.
* Adding **authentication for API write access** (optional).
* Moving media storage to cloud (e.g., S3 or Cloudinary) for production.