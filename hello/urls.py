from django.urls import path
from hello import views

# file is where you specify patterns to route 
# different URLs to their appropriate views
urlpatterns = [
    path("", views.home, name="home"),
]