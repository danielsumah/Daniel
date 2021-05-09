
from django.urls import path

from .views import CreateStudentViews, ReadStudentViews, UpdateStudentViews, DeleteStudentViews

urlpatterns = [
    # path('api', home, name = 'api-home'),
    path('api/create-student', CreateStudentViews.as_view(), name = 'api-create-student'),              #create
    path('api/read-students', ReadStudentViews.as_view(), name = 'api-read-students'),                    #read
    path('api/update-student/<int:pk>', UpdateStudentViews.as_view(), name = 'api-update-student'),     #update
    path('api/delete-student/<int:pk>', DeleteStudentViews.as_view(), name = 'api-delete-student'),     #delete
]
