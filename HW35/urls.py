from django.urls import path
from .views import example_template_view

urlpatterns = [
    path('example/', example_template_view, name='example_template_view'),
]
