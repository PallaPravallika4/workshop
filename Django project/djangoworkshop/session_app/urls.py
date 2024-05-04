from django.urls import path
from session_app import views

urlpatterns = [
    path('set_session/',views.set_session,name='set'),
    path('get_session/',views.get_session,name='get')
]