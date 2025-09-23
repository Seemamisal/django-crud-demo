# Demo Task - Django CRUD + API Integration + Reporting

## Features
- CRUD APIs for Tasks (`/api/tasks/`)
- External API Integration (`/api/external-tasks/`)
- Simple Data Visualization (`/api/report/`)

## Tech Stack
- Django + DRF
- PostgreSQL (Supabase)
- Matplotlib (for charts)

## Setup
```bash
git clone <repo-url>
cd demo_project
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
