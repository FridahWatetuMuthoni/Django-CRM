from django.urls import path
from . import views

app_name = 'leads'


urlpatterns = [
    path('', views.leads_list, name='leads'),
    path('detail/<str:pk>/', views.leads_detail, name="detail"),
    path('create', views.create_lead, name='create'),
    path('update/<str:pk>/', views.update_lead, name='update'),
    path('delete/<str:pk>/', views.delete_lead, name='delete')
]
