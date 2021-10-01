from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("customer", views.CustomerView)
router.register("vendors", views.VendorsView)
router.register("employs", views.EmploysView)
router.register("category", views.CategoryView)
router.register("product", views.ProductView)
#Demo application urls ...
urlpatterns = [
    path("", include(router.urls)),
]
