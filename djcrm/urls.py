
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from leads.views import landing_page, LandingPageView,SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(),name="landing-page"),
    path('leads/',include('leads.urls', namespace="leads")),
    path('agents/',include('agents.urls', namespace="agents")),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('reset-password/',PasswordResetView.as_view(),name="reset-password"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
