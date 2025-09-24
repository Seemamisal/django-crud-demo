****Demo Task - Django CRUD + API Integration + Reporting****
***Features***

CRUD APIs for Tasks (/api/tasks/)

External API Integration (/api/external-tasks/)

Simple Data Visualization (/api/report/ for PNG, /api/report-json/ for JSON)

***Tech Stack***

Django + Django REST Framework

PostgreSQL (Supabase or Render)

Matplotlib (for charts)

Python 3.13

***Setup***
1. Clone Repository
git clone <repo-url>
cd demo_project

2. Create Virtual Environment & Activate
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Setup Environment Variables

Create a .env file in the project root:

SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost,django-crud-demo.onrender.com
DATABASE_URL=postgresql://USER:PASSWORD@HOST:PORT/DBNAME

5. Apply Migrations
python manage.py migrate

6. Run Locally
python manage.py runserver


Access: http://127.0.0.1:8000/

API Endpoints
Endpoint	Method	Description
/api/tasks/	GET, POST, PUT, DELETE	CRUD operations on tasks
/api/external-tasks/	GET	Fetch first 5 tasks from JSONPlaceholder
/api/report/	GET	Bar chart (PNG) for Completed vs Pending tasks
/api/report-json/	GET	Completed vs Pending task counts as JSON
/test-db/	GET	Test database connection

***Deployment***

You can check the deployed application here:

Public Live URL: https://django-crud-demo.onrender.com/

Admin Panel: https://django-crud-demo.onrender.com/admin/

API: https://django-crud-demo.onrender.com/api/tasks/

Hosted on Render with PostgreSQL backend.

Make sure DEBUG=False in production.

Hosted on Render with PostgreSQL backend.

Make sure DEBUG=False in production.

***Author***

Seema Misal – Full Stack Developer
