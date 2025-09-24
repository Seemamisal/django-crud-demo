from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet, fetch_external_tasks, tasks_report, tasks_report_json, test_db

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/external-tasks/', fetch_external_tasks, name='external-tasks'),
    path('api/report/', tasks_report, name='tasks-report'),
    path('api/report-json/', tasks_report_json, name='tasks-report-json'),
    path('test-db/', test_db, name='test-db'),

    # Home page route
    path('', include('tasks.urls')),  # '/' renders home.html
]
