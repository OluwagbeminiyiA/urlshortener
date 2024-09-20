
---

# 🔗 Django URL Shortener with Sqids

This project is a URL shortening service built with **Django REST Framework (DRF)** and **Sqids** for generating unique, short, and URL-friendly identifiers. This project provides an API to shorten URLs and return custom short URLs for users.

## ✨ Features

- **Shorten URLs**: Generate short URLs using Sqids, ensuring unique and user-friendly identifiers.
- **RESTful API**: Built with Django REST Framework for easy API consumption.
- **Customizable URL generation**: Easily customize the URL encoding logic with `sqids`.
- **Collision-Free**: Ensures that each generated short URL is unique.

## 📦 Tech Stack

- **Backend**: Django, Django REST Framework
- **URL Shortener**: [Sqids](https://github.com/sqids/sqids-python) (Squid-friendly ID Shortener)
- **Database**: SQLite (default) or any Django-supported database (PostgreSQL, MySQL, etc.)
- **Python**: Version 3.7 or higher

## 🚀 Quick Start

Follow these instructions to get a local instance of the project running.

### Prerequisites

- Python 3.7+
- Django 4.0+
- A virtual environment manager (like `venv` or `virtualenv`)

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/oluwagbeminiyiA/urlshortener.git
    cd urlshortener
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the migrations**:

    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

6. **Test the API**:

    Use a tool like [Postman](https://www.postman.com/) or `curl` to interact with the API:

    ```bash
    curl -X POST http://127.0.0.1:8000/ -d "url=http://example.com"
    ```

### Example Response

```json
{
  "key": "B8Zw93",
  "url": "http://127.0.0.1:8000/B8Zw93"
}
```

## 🛠 Project Structure

```bash
django-url-shortener/
├── manage.py
├── urlshortener/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
└── requirements.txt
```

### Key Files

- **models.py**: Defines the `URL` model for storing original URLs.
- **serializers.py**: Handles the serialization of URL data for API responses.
- **views.py**: Contains the logic for creating and retrieving shortened URLs, using `sqids` to generate unique keys.
- **sqids.py**: Integration with the `sqids` library for URL shortening.

## ⚙️ API Endpoints

### POST / (Create a Short URL)

Shortens a provided URL.

- **Request**:

  ```json
  {
    "url": "http://127.0.0.1:8000/"
  }
  ```

- **Response**:

  ```json
    {
      "key": "B8Zw93",
      "url": "http://127.0.0.1:8000/B8Zw93"
    }
  ```
  
### GET /<str:key>/ (Redirects a Shortened URL)

Redirects a provided shortened URL.

- **Request**:

  ```json
  {
    "url": "http://127.0.0.1:8000/B8Zw93"
  }
  ```

- **Response**:

    Redirects to the original url

## 🌟 Customization


- **Database**: The default configuration uses SQLite, but you can configure PostgreSQL or MySQL in your `settings.py` for production use.


## 🛡 Security

To ensure the security of the shortened URLs and the API:

- Use **HTTPS** for serving the API in production.
- Consider adding **rate-limiting** to prevent abuse of the URL shortening service.
- Implement authentication if needed for restricted access to certain endpoints.

## 🤝 Contributing

We welcome contributions! Please follow these steps to contribute to the project:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a pull request

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---