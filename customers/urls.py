from django.urls import path
from . import views


urlpatterns = [
    path("", views.customer_list, name="customer_list"),   # homepage
    path("create/", views.customer_create, name="customer_form"),
    path("update/<int:pk>/", views.customer_update, name="customer_update"),
    path("delete/<int:pk>/", views.customer_delete, name="customer_delete"),
]
