"""
URL configuration for demo_project project.
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet, fetch_external_tasks, tasks_report
from tasks.views import tasks_report, tasks_report_json


# ---------------------------
# Router setup for Task CRUD API
# ---------------------------
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)  # /api/tasks/ route

# ---------------------------
# URL patterns
# ---------------------------
urlpatterns = [
    path('admin/', admin.site.urls),        # Admin panel
    path('api/', include(router.urls)),     # CRUD API under /api/tasks/
    
    # External API fetch
    path('api/external-tasks/', fetch_external_tasks, name='external-tasks'),
    
    # Tasks report chart
    path('api/report/', tasks_report, name='tasks-report'),

    path('api/report/', tasks_report, name='tasks-report'),
    path('api/report-json/', tasks_report_json, name='tasks-report-json'),  # optional

]
