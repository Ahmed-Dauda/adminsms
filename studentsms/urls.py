
from django.urls import path
from . import views

app_name = 'studentsms'

urlpatterns = [
   
    path('', views.index, name = 'index'),
    path('myview', views.myview, name = 'myview'),
    path('add', views.add_students, name = 'add'),
    path('update/<pk>/', views.update_students, name = 'update'),
    path('delete/<pk>/', views.delete_students, name = 'delete'),
    path('pdf_all', views.pdf_all_view, name = 'pdf_all'),
    path('pdf_id/<int:pk>/', views.pdf_id_view, name = 'pdf_id'),
]
