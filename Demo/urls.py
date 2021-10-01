"""Demo URL Configuration


"""

from django.urls import path, include

urlpatterns = [
    path('api/', include('DemoApp.urls'))  #Following the path of demo app site URLs
]
