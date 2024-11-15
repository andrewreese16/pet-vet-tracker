from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("", views.dashboard, name="dashboard"),
    path("add_pet/", views.add_pet, name="add_pet"),
    path("add_visit/<int:pet_id>/", views.add_visit, name="add_visit"),
    path("pets/<int:pet_id>/", views.pet_detail, name="pet_detail"),
    path("update_visit/<int:visit_id>/", views.update_visit, name="update_visit"),
    path("delete_visit/<int:visit_id>/", views.delete_visit, name="delete_visit"),
    path("delete_pet/<int:pet_id>/", views.delete_pet, name="delete_pet"),
]
