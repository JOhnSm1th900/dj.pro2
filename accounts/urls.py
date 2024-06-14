from django.contrib.auth.views import LoginView
from django.urls import path,include
from accounts.views import RegisterView, edit_profile
from accounts.forms import UserLoginForm
from accounts.views import LogoutViewWithGet

urlpatterns = [
    path('login/', LoginView.as_view(authentication_form=UserLoginForm), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', edit_profile, name='profile'),
    path('logout/', LogoutViewWithGet.as_view(), name='logout'),
    path('', include('django.contrib.auth.urls'))
]