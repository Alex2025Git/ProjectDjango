from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import UserCreateView, email_confirm_view, logout_view, UserUpdateView, UserDetailView, UserDeleteView

app_name = UsersConfig.name

urlpatterns = [

   path('login/', LoginView.as_view(template_name='login.html'), name='login'),
   path('logout/', logout_view, name='logout'),
   path('register/', UserCreateView.as_view(), name='register'),
   path('email_confirm/<str:token>/', email_confirm_view, name='email_confirm'),
   path('profile/update/<int:pk>', UserUpdateView.as_view(), name='user_update'),
   path('profile/<int:pk>', UserDetailView.as_view(), name='user_detail'),
   path('profile/delete/<int:pk>', UserDeleteView.as_view(), name='user_delete'),
]