from django.contrib.auth.views import LoginView
from django.urls import path,include

from accounts.forms import UserLoginForm
from accounts.views import LogoutViewWithGet

urlpatterns = [
    path('login/', LoginView.as_view(authentication_form=UserLoginForm),name='login'),
    path('logout/', LogoutViewWithGet.as_view(), name='logout'),  # تمّ التعديل هنا
    path('', include('django.contrib.auth.urls'))
]