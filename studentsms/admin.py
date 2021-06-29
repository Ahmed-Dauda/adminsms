from django.contrib import admin
from studentsms.models import students_reg

# Register your models here.
admin.site.site_title = 'students records'
admin.site.site_header = 'Esteem students management system'
admin.site.register(students_reg)
