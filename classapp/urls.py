from django.urls import path
from .views import students_view, teachers_view, courses_view

urlpatterns = [
    # Admin
    

    # Students
    path('students/', students_view, name='students'),  # list & create
    path('students/<int:student_id>/', students_view, name='students-detail'),  # get/update/delete

    # Teachers
    path('teachers/', teachers_view, name='teachers'),
    path('teachers/<int:teacher_id>/', teachers_view, name='teachers-detail'),

    # Courses
    path('courses/', courses_view, name='courses'),
    path('courses/<int:course_id>/', courses_view, name='courses-detail'),
]
