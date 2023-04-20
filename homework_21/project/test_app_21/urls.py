from django.urls import path
from . import views

urlpatterns = [
    path('quote/<number>', views.MyClassBasedView.as_view(), name='quote_name'), 
    path('factorial/<factorial_json>', views.index, name='factorial_name'), 
]