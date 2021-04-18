from django.urls import path

from .import views
urlpatterns = [
    path("",views.index),
    path("create/user",views.create_user),
    path("employees/<int:employee_id>",views.employee_info),
    path("employees/<int:employee_id>/delete",views.delete_employee),
    path("employees/<int:employee_id>/edit",views.edit_employee),
    path("employees/<int:employee_id>/update",views.update_employee)
]