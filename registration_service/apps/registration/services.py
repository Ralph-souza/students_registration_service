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
            # Log do erro para debug
            error_detail = ""
            try:
                error_detail = response.json()
            except:
                error_detail = response.text[:200]
            
            raise ValidationError(
                f"Erro ao validar estudante no student_service: Status {response.status_code}. "
                f"Detalhes: {error_detail}. URL: {url}"
            )
    except requests.exceptions.RequestException as e:
        # Erro de conexão, timeout, etc
        raise ValidationError(
            f"Erro ao comunicar com student_service: {str(e)}. URL: {url}"
        )
