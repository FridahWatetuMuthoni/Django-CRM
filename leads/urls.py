from django.urls import path
from . import views

app_name = 'leads'


urlpatterns = [
    path('', views.Leads_List_view.as_view(), name='leads'),
    path('detail/<str:pk>/', views.Leads_Detail_View.as_view(), name="detail"),
    path('create', views.Leads_Create_View.as_view(), name='create'),
    path('update/<str:pk>/', views.Leads_Update_View.as_view(), name='update'),
    path('delete/<str:pk>/', views.Leads_Delete_View.as_view(), name='delete')
]
