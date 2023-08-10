from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("logout/", views.logout_user, name = "logout"),
    path("register/", views.register_user, name = "register"),
    path("record/<int:pk>", views.cutomer_record, name = "record"),
    path("delete_record/<int:pk>", views.delete_record, name = "delete_record"),
    # path("record/<int:pk>", views.cutomer_record, name = "record"),
]
