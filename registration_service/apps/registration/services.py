"""
Serviços para comunicação com outros microserviços
"""
import requests

from django.conf import settings
from django.core.exceptions import ValidationError


def validate_student_exists(student_id):
    """
    Valida se um estudante existe no student_service.
    
    Args:
        student_id: UUID do estudante
        
    Returns:
        bool: True se o estudante existe, False caso contrário
        
    Raises:
        ValidationError: Se houver erro na comunicação com o serviço
    """
    student_service_url = getattr(settings, 'STUDENT_SERVICE_URL', 'http://localhost:8000/api/student')
    url = f"{student_service_url}/{student_id}/"
    
    try:
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            return True
        elif response.status_code == 404:
            return False
        else:
            # Se o serviço retornar erro (500, 503, etc), podemos tratar de diferentes formas
            # Por enquanto, vamos considerar como erro de comunicação
            raise ValidationError(
                f"Erro ao validar estudante no student_service: Status {response.status_code}"
            )
    except requests.exceptions.RequestException as e:
        # Erro de conexão, timeout, etc
        raise ValidationError(
            f"Erro ao comunicar com student_service: {str(e)}"
        )
