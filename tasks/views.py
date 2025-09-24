from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.db import connection
import requests
import io

import matplotlib
matplotlib.use('Agg')  # Non-GUI backend for server
import matplotlib.pyplot as plt

from .models import Task
from .serializers import TaskSerializer

# ---------------------------
# 1️⃣ CRUD API (ModelViewSet)
# ---------------------------
class TaskViewSet(viewsets.ModelViewSet):
    """
    Provides full CRUD API for Task model.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# ---------------------------
# 2️⃣ External API fetch
# ---------------------------
@api_view(['GET'])
def fetch_external_tasks(request):
    """
    Fetch first 5 tasks from JSONPlaceholder and return as JSON.
    """
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/todos?_limit=5", 
            timeout=5
        )
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        return Response(
            {"error": "Failed to fetch external tasks", "details": str(e)}, 
            status=500
        )
    return Response(data)


# ---------------------------
# 3️⃣ Tasks report chart (PNG)
# ---------------------------
@api_view(['GET'])
def tasks_report(request):
    """
    Generate a simple bar chart (Completed vs Pending tasks) as PNG.
    """
    completed_count = Task.objects.filter(completed=True).count()
    pending_count = Task.objects.filter(completed=False).count()

    # Create chart
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(['Completed', 'Pending'], [completed_count, pending_count], color=['green', 'red'])
    ax.set_ylabel('Count')
    ax.set_title('Tasks Status Report')
    ax.set_ylim(0, max(completed_count, pending_count) + 5)  # optional padding

    # Save chart to buffer
    buffer = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)

    return HttpResponse(buffer.read(), content_type='image/png')


# ---------------------------
# 4️⃣ Optional: JSON report (for interactive charts)
# ---------------------------
@api_view(['GET'])
def tasks_report_json(request):
    """
    Returns completed vs pending task counts as JSON.
    """
    completed_count = Task.objects.filter(completed=True).count()
    pending_count = Task.objects.filter(completed=False).count()

    return Response({
        "completed": completed_count,
        "pending": pending_count
    })


# ---------------------------
# 5️⃣ DB test endpoint
# ---------------------------
@api_view(['GET'])
def test_db(request):
    """
    Simple endpoint to check DB connection.
    """
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT 1;")
        return HttpResponse("Database OK ✅")
    except Exception as e:
        return HttpResponse(f"Database connection failed ❌: {e}")
