from django.urls import path
from . import views

# This list holds the URL patterns for the `accounts` app.
# Django looks for this variable to find the app's URLs.
urlpatterns = [
    # This path maps the root URL (e.g., yourdomain.com/) to the 'home' view
    # defined in the accounts/views.py file.
    path('', views.home, name='home'),
]
