# Ticketier DRF API

Simple Django + DRF scaffold for the Ticketier project. Features:

- Custom User model (minimal AbstractUser)
- JWT authentication using SimpleJWT
- Device registration endpoint

Run locally:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Auth endpoints (example):

- POST /api/v1/auth/register/  -> register (username, email, password, password2)
- POST /api/v1/token/ -> obtain JWT (username + password)
- POST /api/v1/token/refresh/ -> refresh JWT
- GET  /api/v1/auth/me/ -> current user (requires Authorization: Bearer <token>)

This scaffold focuses on a standard, minimal user model and working JWT auth. Next steps: add events, ticket products, orders, QR generation and verification endpoints.
