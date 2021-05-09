
from django.urls import path

from .views import home, StudentViews

urlpatterns = [
    path('api', home, name = 'api-home'),
    path('api/create-student', StudentViews.as_view(), name = 'api-create-student'),
]
