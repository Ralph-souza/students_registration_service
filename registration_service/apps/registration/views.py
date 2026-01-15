from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Registration
from .serializers import RegistrationSerializer


class RegistrationViewSet(viewsets.ModelViewSet):
    """
    ViewSet para Registration.
    
    A validação do student_id ocorre automaticamente no serializer
    quando um POST ou PUT é feito.
    """
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    
    @action(detail=False, methods=['get'])
    def by_student(self, request):
        """
        Endpoint customizado para buscar registrations por student_id.
        Exemplo: GET /api/registrations/by_student/?student_id=<uuid>
        """
        student_id = request.query_params.get('student_id')
        if not student_id:
            return Response(
                {'error': 'Parâmetro student_id é obrigatório'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        registrations = self.queryset.filter(student_id=student_id)
        serializer = self.get_serializer(registrations, many=True)
        return Response(serializer.data)
