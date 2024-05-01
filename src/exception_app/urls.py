from django.urls import path
from . import views

urlpatterns = [
    path('exception/', views.trigger_exception, name='trigger_exception'),
]
