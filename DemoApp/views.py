from rest_framework import generics
from rest_framework import viewsets, filters
from .models import Customers, Vendors, Employees, Category, Product
from .serializers import CustomerSerializer, VendorSerializer, EmploySerializer, CategorySerializer, ProductSerializer


class CustomerView(viewsets.ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer

class VendorsView(viewsets.ModelViewSet):
    queryset = Vendors.objects.all()
    serializer_class = VendorSerializer

class EmploysView(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmploySerializer

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




'''class ApiRoot(generics.GenericAPIView):
    name = 'Demo-api-Root'

    def get(self, request, *args, **kwargs):
        return Response({
            "Customers Info": reverse(CustomerList.name, request=request),
            "Vendors Info  ": reverse(VendorsList.name, request=request),
            "Employees Info": reverse(EmploysList.name, request=request),
            })
'''