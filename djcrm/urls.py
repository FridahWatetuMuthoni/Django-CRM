from django.contrib import admin
from django.urls import path, include
from leads.views import Home_Page_View
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls', namespace="leads")),
    path('', Home_Page_View.as_view(), name="home"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout")
]

if settings.DEBUG:
    urlpatterns + static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)
