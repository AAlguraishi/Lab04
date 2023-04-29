from django.urls import path
from . import views
urlpatterns=[
    path("",views.firstView,name="tax"),
    path("<int:num>",views.secondView,name="num"),
    path("taxrate",views.thirdView,name="rate")
    ]