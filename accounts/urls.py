from django.urls import path

from .views import (
    RegisterView,
    LoginView,
    ProfileView,
)

from .admin_views import (
    AdminEmployeeListAPIView,
    AdminEmployeeTrackerAPIView,
)


urlpatterns = [

    path(
        "register/",
        RegisterView.as_view(),
        name="register"
    ),

    path(
        "login/",
        LoginView.as_view(),
        name="login"
    ),

    path(
        "profile/",
        ProfileView.as_view(),
        name="profile"
    ),

    path(
        "admin/employees/",
        AdminEmployeeListAPIView.as_view(),
        name="admin-employees"
    ),

    path(
        "admin/employees/<int:employee_id>/tracker/",
        AdminEmployeeTrackerAPIView.as_view(),
        name="admin-employee-tracker"
    ),

]