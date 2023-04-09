from django.urls import path

from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("",views.ListProductAPIView.as_view(),name="Product_list"),
    path("create/", views.CreateProductAPIView.as_view(),name="Product_create"),
    path("update/<int:pk>/",views.UpdateProductAPIView.as_view(),name="update_Product"),
    path("delete/<int:pk>/",views.DeleteProductAPIView.as_view(),name="delete_Product")

]