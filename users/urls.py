from django.urls import path
from django.contrib.auth import views as authentication_views
from .views import logout_page, profile_page, write_message, get_inbox, all_profiles
urlpatterns = [
    path('login/', authentication_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', logout_page, name='logout'),
    path('profile/', profile_page, name='profile'),
    path('send_message/', write_message, name='send_message'),
    path('inbox/',get_inbox, name='inbox'),
    path('profiles/', all_profiles, name = 'allProfiles'),

 ]