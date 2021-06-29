import django_filters
from studentsms.models import students_reg

class StudentsFilter(django_filters.FilterSet):
    class Meta:
        model = students_reg
        fields = {
            'names': ['icontains'],
            'level': ['iexact'],
            'admin_no': ['iexact']
        }