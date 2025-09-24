"""
URL configuration for demo_project project.
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import (
    TaskViewSet, fetch_external_tasks, tasks_report, 
    tasks_report_json, test_db
)

# ---------------------------
# Router setup for Task CRUD API
# ---------------------------
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')  # /api/tasks/ route

# ---------------------------
# URL patterns
# ---------------------------
urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # CRUD API routes via router
    path('api/', include(router.urls)),

    # External tasks fetch
    path('api/external-tasks/', fetch_external_tasks, name='external-tasks'),

    # Tasks report chart (PNG)
    path('api/report/', tasks_report, name='tasks-report'),

    # Tasks report JSON (for frontend/interactive charts)
    path('api/report-json/', tasks_report_json, name='tasks-report-json'),

    # ✅ DB test endpoint
    path('test-db/', test_db, name='test-db'),
]
