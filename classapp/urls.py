# classapp/urls.py
from django.urls import path
from .views import (
    students_view, teachers_view, courses_view,
    register_view, success_view,
    login_view, logout_view, dashboard_view
)

urlpatterns = [
    # Students
    path('students/', students_view, name='students'),
    path('students/<int:student_id>/', students_view, name='students-detail'),

    # Teachers
    path('teachers/', teachers_view, name='teachers'),
    path('teachers/<int:teacher_id>/', teachers_view, name='teachers-detail'),

    # Courses
    path('courses/', courses_view, name='courses'),
    path('courses/<int:course_id>/', courses_view, name='courses-detail'),

    # Auth
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("success/", success_view, name="success"),
]
