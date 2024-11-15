from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("", views.dashboard, name="dashboard"),
    path("add_pet/", views.add_pet, name="add_pet"),
    path("add_visit/<int:pet_id>/", views.add_visit, name="add_visit"),
    path("pets/<int:pet_id>/", views.pet_detail, name="pet_detail"),
]
