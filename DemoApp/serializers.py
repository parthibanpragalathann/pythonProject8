from rest_framework import serializers
from .models import Customers, Vendors, Employees, Category, Product

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customers
        fields = ('url',
                  'pk',
                  'name',
                  'ph_no',
                  'gender',
                  'date',
                  'cus_type')

class VendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendors
        fields = ('url',
                  'pk',
                  'name',
                  'ph_no',
                  'gender',
                  'date',
                  'ven_type')

class EmploySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields = ('url',
                  'pk',
                  'name',
                  'ph_no',
                  'gender',
                  'date',
                  'emp_type')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url',
                  'pk',
                  'name')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('url',
                  'pk',
                  'category',
                  'name',
                  'quantity',
                  'price')
