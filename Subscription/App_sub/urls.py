from django.urls import path, include
from .views import Sub_body, Subscribe
urlpatterns = [
    path('register/', Sub_body.as_view(), name = 'register' ),
    path('subs/',  Subscribe.as_view(), name='subscribe'),
]