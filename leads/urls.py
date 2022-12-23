from django.urls import path
from . import views

app_name = 'leads'


urlpatterns = [
    path('', views.Leads_List_view.as_view(), name='leads'),
    path('detail/<str:pk>/', views.Leads_Detail_View.as_view(), name="detail"),
    path('create', views.Leads_Create_View.as_view(), name='create'),
    path('update/<str:pk>/', views.Leads_Update_View.as_view(), name='update'),
    path('delete/<str:pk>/', views.Leads_Delete_View.as_view(), name='delete'),
    path('assign/<str:pk>/', views.AssignAgentView.as_view(), name='assign'),
    path('categories', views.CategoryListView.as_view(), name='categories'),
    path('category/details/<str:pk>/',
         views.CategoryDetailView.as_view(), name='category_detail'),
    path('category/update/<str:pk>/',
         views.CategoryUpdateView.as_view(), name='category_update'),
    path('<int:pk>/followups/create/',
         views.FollowUpCreateView.as_view(), name='lead-followup-create'),
    path('followups/<int:pk>/', views.FollowUpUpdateView.as_view(),
         name='lead-followup-update'),
    path('followups/<int:pk>/delete/',
         views.FollowUpDeleteView.as_view(), name='lead-followup-delete'),


]
