from django.urls import path
from . import views

app_name = 'agents'

urlpatterns = [
    path('', views.AgentsListView.as_view(), name='agents_list'),
    path('create/', views.AgentsCreateView.as_view(), name='agents_create'),
    path('detail/<str:pk>/', views.AgentDetailView.as_view(), name='agents_detail'),
    path('update/<str:pk>/', views.AgentUpdateView.as_view(), name="agents_update"),
    path('delete/<str:pk>/', views.AgentDeleteView.as_view(), name='agents_delete')
]
