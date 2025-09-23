from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
import requests
import io

import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend for server environments
import matplotlib.pyplot as plt

from .models import Task
from .serializers import TaskSerializer

# ---------------------------
# 1️⃣ CRUD API (ModelViewSet)
# ---------------------------
class TaskViewSet(viewsets.ModelViewSet):
    """
    Provides full CRUD API for Task model
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# ---------------------------
# 2️⃣ External API fetch
# ---------------------------
@api_view(['GET'])
def fetch_external_tasks(request):
    """
    Fetch tasks from JSONPlaceholder (limit 5) and return as JSON.
    """
    try:
        r = requests.get("https://jsonplaceholder.typicode.com/todos?_limit=5", timeout=5)
        r.raise_for_status()
        data = r.json()
    except requests.RequestException as e:
        return Response({"error": "Failed to fetch external tasks", "details": str(e)}, status=500)
    return Response(data)

# ---------------------------
# 3️⃣ Tasks report chart (PNG)
# ---------------------------
@api_view(['GET'])
def tasks_report(request):
    """
    Generate a bar chart: completed vs pending tasks
    """
    completed = Task.objects.filter(completed=True).count()
    pending = Task.objects.filter(completed=False).count()

    # Create chart
    fig, ax = plt.subplots()
    ax.bar(['Completed', 'Pending'], [completed, pending], color=['green', 'red'])
    ax.set_ylabel('Count')
    ax.set_title('Tasks Status Report')

    # Save chart to buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)

    return HttpResponse(buf.read(), content_type='image/png')

# ---------------------------
# 4️⃣ Optional: JSON report (for interactive charts)
# ---------------------------
@api_view(['GET'])
def tasks_report_json(request):
    """
    Returns completed vs pending task counts as JSON
    """
    completed = Task.objects.filter(completed=True).count()
    pending = Task.objects.filter(completed=False).count()
    return Response({"completed": completed, "pending": pending})
