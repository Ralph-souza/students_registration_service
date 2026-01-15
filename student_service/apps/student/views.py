from drf_jsonmask.views import OptimizedQuerySetMixin
from rest_framework import viewsets

from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(OptimizedQuerySetMixin, viewsets.ModelViewSet):
    http_method_names = ["get", "post", "put", "delete"]
    queryset = Student.objects.all().order_by("created_at")
    serializer_class = StudentSerializer
