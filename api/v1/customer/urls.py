from django.urls import path
from api.v1.customer import views


urlpatterns = [
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("categories/", views.categories, name="categories"),
    path("add_category/", views.add_category, name="add_category"),
    path("edit_category/<int:id>/", views.edit_category, name="edit_category"),
    path("delete_category/<int:id>/", views.delete_category, name="delete_category"),
    path("products/", views.products, name="products"),
    path("add_product/", views.add_product, name="add_product"),
    path("edit_product/<int:id>/", views.edit_product, name="edit_product"),
    path("delete_product/<int:id>/", views.delete_product, name="delete_product"),
]
