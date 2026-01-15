from rest_framework import serializers

from .models import Registration
from .services import validate_student_exists


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer para Registration com validação de student_id
    """
    
    class Meta:
        model = Registration
        fields = [
            'id',
            'student_id',
            'email',
            'phone',
            'gender',
            'degree',
            'contact_name',
            'contact_number',
            'relationship',
        ]
        read_only_fields = ['id']
    
    def validate_student_id(self, value):
        """
        Valida se o student_id existe no student_service.
        Esta validação ocorre automaticamente quando o serializer é usado.
        """
        if not validate_student_exists(value):
            raise serializers.ValidationError(
                f"Estudante com ID {value} não encontrado no student_service."
            )
        return value
