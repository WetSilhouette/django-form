# Django Job Application Form

A Django web application for collecting and managing job applications with email notifications.

## Features

- **Responsive Form Interface**: Bootstrap-styled job application form
- **Data Validation**: Server-side form validation using Django forms
- **Database Storage**: Stores application data in SQLite database
- **Email Notifications**: Sends confirmation emails to applicants upon submission
- **Success Messages**: User-friendly feedback using Django messages framework
- **Admin Interface**: Django admin panel for managing applications

## Project Structure

```
django-form/
├── job_application/          # Main application
│   ├── models.py            # Form data model
│   ├── forms.py             # Django form definition
│   ├── views.py             # View logic
│   ├── urls.py              # App URL configuration
│   ├── admin.py             # Admin configuration
│   └── templates/
│       └── index.html       # Job application form template
├── mysite/                  # Project configuration
│   ├── settings.py          # Django settings
│   ├── urls.py              # Root URL configuration
│   └── wsgi.py              # WSGI configuration
├── manage.py                # Django management script
├── db.sqlite3               # SQLite database
└── pyproject.toml           # Project dependencies
```

## Requirements

- Python >= 3.13
- Django >= 6.0.3
- dotenv >= 0.9.9

