# LibraryProject

This Django project demonstrates:
- A custom user model (`accounts.CustomUser`).
- Permissions and groups (e.g., `can_view`, `can_create`, `can_edit`, `can_delete`).
- Security best practices:
  - CSRF protection
  - Secure cookies
  - XSS and clickjacking protection
  - Custom permissions in views

## Apps
- **accounts** → Custom user management
- **bookshelf** → Book model, permissions, and views

## How to Run
```bash
python3 manage.py runserver
