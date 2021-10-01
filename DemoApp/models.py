from django.db import models

# Create your models here.
gender_type = (("Male", "Male"), ("Female", "Female"), ("Trans", "Trans"))
customer_type = (("New Customer", "New Customer"), ("Exist Customer", "Exist Customer"))
vendor_type = (("New Vendor", "New Vendor"), ("Exist Vendor", "Exist Vendor"))
employ_type = (("Manager", "Manager"), ("Staff", "Staff"), ("Admin", "Admin"))

class Contact(models.Model):
    name = models.CharField(max_length=110)
    ph_no = models.CharField(max_length=10, unique=True)
    gender = models.CharField(max_length=10, choices=gender_type)
    date = models.DateField(auto_now_add=True)
    class Meta:
        abstract=True

class Customers(Contact):
    cus_type = models.CharField(max_length=20, choices=customer_type, default="New Customer")
    def __str__(self):
        return self.name
class Vendors(Contact):
    ven_type = models.CharField(max_length=20, choices=vendor_type, default="New Vendor")
    def __str__(self):
        return self.name
class Employees(Contact):
    emp_type = models.CharField(max_length=20, choices=employ_type, default="Staff")

    def __str__(self):
        return self.name

#Many to One Relationship
class Category(models.Model):
    name = models.CharField(max_length=110)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    name = models.CharField(max_length=110)
    quantity = models.IntegerField()
    price = models.FloatField()
